s1='welcome'
s2='homely'
s3=s1.upper()
s4=s2.upper()
if sorted(s3)==sorted(s4):
    print(s1,"and",s2,"anagram")
else:
    print(s1,"and",s2,"are not anagram")
