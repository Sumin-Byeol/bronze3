# Dissatisfied with the loud and constant pronouncements of his alleged misdeeds
# by a trio of indefatigable minstrels,
# the brave knight Sir Robin wishes to exercise his authority by modifying their lyrics.
# The minstrels were happy to provide printed transcripts of their songs,
# and cheerfully announced that they would not change a word of them.

# Undaunted, the brave (and crafty) Sir Robin scrutinized the documents and
# noticed that their loudest inflections were indicated by capital letters and
# realized that he could at least lower their voices. This, he reasoned,
# could be accomplished by replacing upper case letters with lower case letters
# (“Case correction”, from his perspective).
# These modifications could be forced upon the singers by
# insistence upon proper usage of the King’s English.
# Not all letters can be lower case, however,
# as the King’s English mandates some letters must be upper case.

# Strangely hesitant about performing “case correction” personally,
# the brave, crafty (and managerially capable) Sir Robin humbly requests you
# write a program to perform a first pass of case correction for the songs.
# There will still be some corrections required after this program is used.

# As your program reads the file, it must force to upper case all alphabetic characters
# that follow terminal punctuation marks (period, question mark, and exclamation point)
# with only white space or parentheses characters following.
# All other alphabetic characters are to be forced to lower case.
# Note that decimal numbers are not to be followed by an upper case character unless the number
# itself is followed by a terminal punctuation mark.

# 입력
# The input file contains the text that you are converting.
# Your conversions should be based on the rules given by Brave Sir Robin above.

# 출력
# The output is to be the converted text. All characters are transferred to the output.
# Some will have cAsE cOrReCtiOn, others will be directly copied.

import re
import sys


s = sys.stdin.readline().rstrip()  #  문장 입력
s = s.lower()  # 전체 문장 소문자로
s = re.sub(r"(?<=[.!?,()]\s)|[.!?,()](\w)", lambda s: s.group().upper(), s)
print(s)
