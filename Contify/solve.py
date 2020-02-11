#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
import itertools
import fileinput, string
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet
import random
from pprint import pprint

stop_words = set(stopwords.words("english"))
    
class Data(object):
    """
    Do input/output and sanity testing of input. Raise Data.Error
    
    Use Case: press 'Ctrl + D' for terminate
    
    >>> d = Data(para="my name is Grijesh Chauhan.",
                 questions="What is my name", 
                 answers="Grijesh Chauhan;Brijesh Chauhan"
                )
    >>> d.validate()
    or use cmd....
    >>> d = Data()
    >>> d.input()
    My name is Grijesh Chauhan.
    what is your name?                
    Grijesh; Brijesh Chauhan
    >>>
    >>> d.validate()
    >>> d.para
    'My name is Grijesh Chauhan.'
    >>> d.questions
    ['what is your name?']
    >>> d.answers
    ['Grijesh', ' Brijesh Chauhan']
    >>>
    """

    class Error(Exception):
        pass
        
    def __init__(self, para=None, questions=None, answers=None):
        self.para = para
        self.questions = questions
        self.answers = answers

    def _split(self, answers):
        if not answers:
            return []
        try:
            return answers.split(';')
        except AttributeError:
            return answers
            
    def validate(self):
        self.answers = self._split(self.answers)
        if not (self.para and self.questions and self.answers):
            if self.para or self.questions or self.answers:
                raise self.Error("Invalid Input")
            raise self.Error("Please enter Para, Questions and ; seprated Answers")
        if len(self.questions) >  len(self.answers):
            raise self.Error("Invalid Input: less answers than questions")

    def input(self):
        lines = []
        for line in fileinput.input():
            line = line.strip().decode('ascii', 'ignore')
            if not line:
                continue
            lines.append(line)
        try:
            self.para, self.questions, self.answers = lines[0], lines[1:-1], lines[-1]
        except IndexError:
            self.para = self.questions = self.answers = None
            
class Question(object):

    def __init__(self, question):
        self.question = question
        self.qtype = None
        self.verb = None
        self.attrs = []
        self.suffix = []
        
    GRAMMAR = r"""
    TYPE: {<WP|WRB|WDT|JJ>}        # What How, Which, Why etcs
    ATTRIBUTE: {<NN.?|JJR|JJS>*}   # which 'color', what 'part' of body, What 'currency' is used
    VERB: {<VB.?|MD>}              # is, can, are, does etcs
    PREP: {<IN|DT|TO>*}            # prepositions - not intresed words!
    """
    Parser = nltk.RegexpParser(GRAMMAR)
    
    def tree(self):
        words = word_tokenize(self.question)
        tagged = nltk.pos_tag(words)
        return self.Parser.parse(tagged)
    
    def analyse(self):
        for subtree in self.tree().subtrees():
            if (not self.qtype) and subtree.label() == "TYPE":
                self.qtype = subtree.leaves()[0][0]
            elif (not self.verb) and subtree.label() == "VERB":
                self.verb = subtree.leaves()[0][0]
            elif (not self.verb) and subtree.label() == "ATTRIBUTE":
                self.attrs.extend(word for word, _ in subtree.leaves())
            elif self.verb and subtree.label() != "PREP":
                self.suffix.extend(word for word, _ in subtree.leaves()
                                        if word not in string.punctuation
                                  )
                                  
    def __repr__(self):
        return "Question<%(qtype)s %(attrs)s %(verb)s %(suffix)s>" % self.__dict__

class ParsedData(Data):
    """ Parse Para into Sentances, Question into Semantics """
    
    @staticmethod
    def itext_tokenize(text, remove_stopwords=False):
        # better to put in utils.py
        """ returns sentence by sentence words"""
        ignore_words = stop_words if remove_stopwords else set()
        ignore_words.update(string.punctuation)
        for sent in sent_tokenize(text):
            words = word_tokenize(sent)
            yield [ word for word in words if word not in ignore_words ]
        
    def tokenized_para(self, remove_stopwords=False):
        return self.itext_tokenize(self.para, remove_stopwords)
        
    def tokenized_answer(self, i, remove_stopwords=True):
        try:
            return self.itext_tokenize(self.answers[i], remove_stopwords).next()
        except IndexError:
            raise self.Error("No Answer: There are only %d answers" % len(self.answers))
        
    def question_analyser(self, i):
        try:
            question = Question(self.questions[i])
            question.analyse()
            return question
        except IndexError:
            raise self.Error("No Question: There are only %d questions" % len(self.questions))
            
class Process(object):

    class Error(Exception):
        pass
    
    def __init__(self, parsed_data):
        self.parsed_data = parsed_data
        self.tokenized_para = tuple(parsed_data.tokenized_para())
        self.analysed_questions = [ parsed_data.question_analyser(i)
                                    for i in range(len(parsed_data.questions)) 
                                  ]
        self.tokenized_answers = [  parsed_data.tokenized_answer(i)
                                    for i in range(len(parsed_data.answers))         
                                 ]
                                 
    @staticmethod
    def similarity(word1, word2):
        try:
            score = wordnet.synsets(word1)[0].wup_similarity( wordnet.synsets(word2)[0])
        except IndexError:
            return 0.0
        return score if score else 0.0
            
    def calculate_similarity(self, words1, words2):
        """ all words in words1 in words2 """
        if len(words1) == 0:
            return 0.0
        similarities =[ max(self.similarity(word1, word2) for word2 in words2)
                        for word1 in words1
                      ]
        return sum(similarities) / len(words1)
        
    def locate(self, analysedQ, tokenized_para):
        """ discovers answering sentences within the para for `i` th question """
        max_score, sents = (0, 0), []
        for tokenized_sent in tokenized_para:
            score = (
                self.calculate_similarity(analysedQ.suffix, tokenized_sent),
                self.calculate_similarity(analysedQ.attrs, tokenized_sent)
            )
            if score > max_score:
                max_score = score
                sents = [tokenized_sent]
            elif max_score == score:
                sents.append(tokenized_sent)
        return sents
        
    def select_answer(self, analysedQ, tokenized_sents):
    
        question_words = set(itertools.chain(analysedQ.attrs, analysedQ.suffix))
        
        def cal_score(tokenized_answer, tokenized_sent):
            answer_words = set(tokenized_answer) - question_words
            if set(tokenized_answer) - set(tokenized_sent):
                score = (0.0, 0.0)
            else:
                score = (
                    self.calculate_similarity(tokenized_answer, tokenized_sent),
                    self.calculate_similarity(answer_words, tokenized_sent),
                )
            return score
                
        max_score, indexs = (0, 0), []
        for i, tokenized_answer in enumerate(self.tokenized_answers):
            score = max(cal_score(tokenized_answer, sent) for sent in tokenized_sents)
            if score > max_score:
                max_score = score
                indexs = [i]
            elif max_score == score:
                indexs.append(i)
                
        if len(indexs) == 0:
            raise self.Error("Answer not found")
        if len(indexs) == 1:
            return self.parsed_data.answers[indexs[0]]
        
        answers = self.locate(analysedQ, (self.tokenized_answers[i] for i in indexs))
        if len(answers) > 1:
            # we can apply Q&A matching...
            answers = [ random.choice(answers) ]
            
        index = self.tokenized_answers.index(answers[0])
        return self.parsed_data.answers[index]
        
def testme():
    para = """Zebras are several species of African equids (horse family) united by their distinctive black and white stripes. Their stripes come in different patterns, unique to each individual. They are generally social animals that live in small harems to large herds. Unlike their closest relatives, horses and donkeys, zebras have never been truly domesticated. There are three species of zebras: the plains zebra, the Grévy's zebra and the mountain zebra. The plains zebra and the mountain zebra belong to the subgenus Hippotigris, but Grévy's zebra is the sole species of subgenus Dolichohippus. The latter resembles an ass, to which it is closely related, while the former two are more horse-like. All three belong to the genus Equus, along with other living equids. The unique stripes of zebras make them one of the animals most familiar to people. They occur in a variety of habitats, such as grasslands, savannas, woodlands, thorny scrublands, mountains, and coastal hills. However, various anthropogenic factors have had a severe impact on zebra populations, in particular hunting for skins and habitat destruction. Grévy's zebra and the mountain zebra are endangered. While plains zebras are much more plentiful, one subspecies, the quagga, became extinct in the late 19th century – though there is currently a plan, called the Quagga Project, that aims to breed zebras that are phenotypically similar to the quagga in a process called breeding back."""
    
    questions = """Which Zebras are endangered?
What is the aim of the Quagga Project?
Which animals are some of their closest relatives?
Which are the three species of zebras?
Which subgenus do the plains zebra and the mountain zebra belong to?""".split("\n")

    answers = """subgenus Hippotigris;the plains zebra, the Grévy's zebra and the mountain zebra;horses and donkeys;aims to breed zebras that are phenotypically similar to the quagga;Grévy's zebra and the mountain zebra"""
    
        
    parsed_data = ParsedData(para=para, questions=questions, answers=answers)
    parsed_data.validate()
    self = Process(parsed_data)
    for analysed_question in self.analysed_questions:
        try:
            sents = self.locate(analysed_question, self.tokenized_para)
            print ( self.select_answer(analysed_question, sents))
        except self.Error as e:
            print (">> %s" % e)
            
def main():
    parsed_data = ParsedData()
    print ("Please enter Para, questions and answers. Press 'Ctrl + D'\n\n")
    parsed_data.input()
    parsed_data.validate()
    
    self = Process(parsed_data)    
    for analysed_question in self.analysed_questions:
        try:
            sents = self.locate(analysed_question, self.tokenized_para)
            print (self.select_answer(analysed_question, sents))
        except self.Error as e:
            print (">> %s" % e)
            
if __name__ == '__main__':
    main()
