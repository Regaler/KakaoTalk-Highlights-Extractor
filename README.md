# KakaoTalk-Highlights-Extractor
0. Intro
In a kakaotalk messenger file, major Korean messenger, you can extract the highlights of conversation with this program. Easy.
How do you recognize the highlights?? I counted the number of 'kiyeok's, that's the sign for 'laughter' in Korean messenger.
It's like, 'hahaha' or 'lololol'.
In Kakaotalk, there's EXPORT function to backup your conversations. You should do that first to get your raw data.
If the program found a line with more than 10 'kiyeok's, for example, it tries to expand the range a bit to include surrounding lines.
Because the specific lines with 10 kiyeoks are not so much.
With that line on the center, we can think the near lines involved are the highlight.

The process is divided into 3
original data -> feature data (kiyeok_counter.py): From original data, extract the features. The criterion may change.
feature data -> step partitions (analyzer.m): Analyze the feature data, and extract the line infos of highlights.
step partitions -> highlights (collector.py): With the step partition data, gather them to make a single highlights file.

1. Environment
Linux (I used cygwin in Windows 64bit), python2.7, matlab 2014 b

2. Programs
kiyeok_counter.py: 
analyzer.m: 
expander.m: 
left_expander.m: 
right_expander.m: 
collector.py: 
text_highlight_extractor.c: 
text_highlight_extractor.exe: 

3. How to run
$ ./text_highlight_extractor textfile.txt

4. Result
result.txt
