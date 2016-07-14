# Text-Reuse

This repository contains code, documentation and slides for the text reuse session at UCREL summer school 2016.

Running Python scripts

Run these four scripts, one by one, by typing the following commands at the command window (cmd.exe)

<h4>1. Text reuse detection with word uni-grams overlap</h4>
<code>
E:\python\python.exe tr-ngram1.py E:\s8-text-reuse\Corpus E:\s8-text-reuse\output tr-unigram
</code>
<br \><br \>
<h4>2. Text reuse detection with word uni-grams overlap + stopwords removed</h4>
<code>
E:\python\python.exe tr-ngram2.py E:\s8-text-reuse\Corpus E:\s8-text-reuse\output tr-unigram-swr
</code>

If this gives an error, you need to download/install <i>stopwords</i> within NLTK.

Type;

<code>
E:\python\python.exe
</code>

<code>
import nltk
</code>

<code>
nltk.download()
</code>

Search/select <b>stopwords</b> from the list of available resources (Corpora [second tab]), click download

<br \><br \>
<h4>3. Text reuse detection with word uni-grams overlap + stopwords removed + Lemmatization</h4>
<code>
E:\python\python.exe tr-ngram2.py E:\s8-text-reuse\Corpus E:\s8-text-reuse\output tr-unigram-swr-lemma
</code>

<br \><br \>
<h4>4. Text reuse detection with word bi-grams (tri-grams) overlap [stopwords removed + Lemmatization]</h4>
<code>
E:\python\python.exe tr-ngram2.py E:\s8-text-reuse\Corpus E:\s8-text-reuse\output tr-bigram
</code>


Running WEKA GUI

<code>
java -jar E:\weka-3-8-0\weka.jar
</code>



