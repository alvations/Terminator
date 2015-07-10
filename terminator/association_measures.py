#!/usr/local/lib/ python3 -*- coding: utf-8 -*-

import math

def prob(x, model):
    return math.exp(model.score(x))

def logprob(x, model):
    return model.score(x)

def joint_prob(x, y, model):
    xy = x + ' ' + y
    return math.exp(model.score(xy))

def marginal_prob(x, y, model, p_xy=None):
    """
    Marginal probability:  p(x,y') = p(X=x, Y!=y)
    """
    if not p_xy:
        p_xy = joint_prob(x,y, model)
    return prob(x, model) - p_xy
    
def conditional_prob(x, y, model):
    """
    Bayesian assumption: p(x|y) = p(x,y) / p(y)
    """
    return math.exp(joint_prob(x, y, model) / float(model.score(y))) 

def pointwise_mutual_information(x, y, model):
    """
    Pointwise Mutual Info: pmi(x,y) = log ( p(xy)/ (p(x,y')*p(x',y)) )
    where p(x,y')and p(x',y) are marginal probabilities
    """
    p_xy = joint_prob(x,y, model)
    p_xnoty = marginal_prob(x, y, model, p_xy)
    p_ynotx = marginal_prob(y, x, model, p_xy)
    try:
        return math.log(p_xy / (p_xnoty * p_ynotx))
    except:
        return 0

def mutual_dependency(x, y, model):
    """
    Mutual Dependency: md(x,y) = log ( p(xy)^2 / (p(x,y')*p(x',y)))
    """
    p_xy = joint_prob(x,y, model)
    p_xnoty = marginal_prob(x, y, model, p_xy)
    p_ynotx = marginal_prob(y, x, model, p_xy)
    return math.log(p_xy*p_xy / (p_xnoty * p_ynotx))

def log_biased_md(x, y, model):
    """
    Log Biased Mutual Dependency: log_biased_md(x,y) = md(x,y) + log(p(xy))
    """
    p_xy = joint_prob(x,y, model)
    p_xnoty = marginal_prob(x, y, model, p_xy)
    p_ynotx = marginal_prob(y, x, model, p_xy)
    return math.log(p_xy*p_xy / (p_xnoty * p_ynotx)) + math.log(p_xy)

def fair_point_expectation(query_ngram, model):
    """
    Fair point expectation: FPE(w1...wn) = 1/n ∑ p(w0...wi)
    e.g.  FPE(the small house) = 1/3(p(the) + p(the small) + p(the small house)) 
    """
    sum_prob, prev = 0, ""
    for w in query_ngram:
        ng = prev + " " + w
        sum_prob += prob(ng.strip())
    return sum_prob / float(len(query_ngram))
        
def normalize_expectation(query_ngram, model):
    """
    Normalize Expectation: NE = p(w1...wn) / FPE(w1...wn)
    """
    p_ngram = prob(" ".join(query_ngram))
    fep =  fair_point_expectation(query_ngram, model)
    return p_ngram / fep

def mutual_expectation(x, y, model):
    """
    Mutual Expectation: ME = p(xy) * NE(xy) 
    """
    p_ngram = prob(x + ' ' + y)
    fep =  fair_point_expectation([x,y], model)
    return p_ngram*p_ngram / fep

def salience(x, y, model):
    """
    Salience: sal(x,y) = md(x,y) * log(p(xy))
    """
    p_xy = joint_prob(x,y, model)
    p_xnoty = marginal_prob(x, y, model, p_xy)
    p_ynotx = marginal_prob(y, x, model, p_xy)
    return math.log(p_xy*p_xy / (p_xnoty * p_ynotx)) * math.log(p_xy)

def lmscore(_ngram, model, measure):
    prev = ""
    measure_sum = []
    for ng in _ngram.split():        
        if prev:
            try:
                this_measure = measure(prev, ng, model)
            except:
                this_measure = 0
            measure_sum.append(this_measure)
        else:
            prev = ng
        prev += " " + ng
    return sum(measure_sum) / float(len(_ngram.split()))

def lmpmi(_ngram, model, measure=pointwise_mutual_information):
    return lmscore(_ngram, model, measure)

def lmpmi_freq(_ngram, model, measure=pointwise_mutual_information):
    return lmscore(_ngram, model, measure) * prob(_ngram, model)
     