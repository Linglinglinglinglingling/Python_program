def count_occurrence(string):
    occurrence_dictionary={}
    for i in string:
        occurrence_dictionary[i]=occurrence_dictionary.get(i,0)+1
    return occurrence_dictionary

a=count_occurrence('This is a really good chance')
print(a)