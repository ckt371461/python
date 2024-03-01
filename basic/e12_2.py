import re
mammoth='''We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze --
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees --
Or as the leaves upon the trees --
It did require to make thee please,
And stand unrivalled Queen of Cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.

Of the youth -- beware of these --
For some of them might rudely squeeze
And bite your cheek; then songs or glees
We could not sing o' Queen of Cheese.

We'rt thou suspended from baloon,
You'd cast a shade, even at noon;
Folks would think it was the moon
About to fall and crush them soon.'''
pat1=r'\bc\w*\b'
#沒有加r的話\b會被辨識錯誤
begin_with_c=re.findall(pat1,mammoth)
print(begin_with_c)
pat2=r'\bc\w{3}\b'
#沒有以\b結尾的話結果會變成['chee', 'city', 'chee', 'coul', 'cast', 'crus']
four_letters_begin_with_c=re.findall(pat2,mammoth)
print(four_letters_begin_with_c)
pat3=r"\b[\w']*r\b"
end_with_r=re.findall(pat3,mammoth)
print(end_with_r)
pat4=r'\b\w*[^aeiou][aeiou]{3}[^aeiou\s]?\w*\b'
# pat4=r'\b\w*[aeiou]{3}\w*\b' 如果這樣寫可能會出四連母音或以上
# pat4=r'\b\w*[^aeiou][aeiou]{3}[^aeiou]\w*\b' 結果會是['Queen', 'quietly', 'beau\nIn', 'Queen', 'squeeze', 'Queen']
# pat4=r'\b\w*[^aeiou][aeiou]{3}[^aeiou\s]\w*\b' 會缺少beau
three_consequent_vowel=re.findall(pat4,mammoth)
print(three_consequent_vowel)