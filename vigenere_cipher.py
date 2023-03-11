
from math import gcd
import string
import numpy as np

# English letter probability
probability_alpha = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.0236,0.0015,0.01974,0.00074]
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# Method for Left shift operation
def shift_left(probability, shift):
    return probability[shift:] + probability[:shift]
# Number to character operation
asciiConverter = dict(zip(range(0,26),string.ascii_lowercase))
# Calculate for 2 to 30 coincidences
def calculateCoincidences(cipherText, copyCipherText):
    counter=0
    countCoincidences=[]
    for k in range(2, 31):
        copyCipherText = np.roll(copyCipherText,1)
        for i,j in zip(cipherText,copyCipherText):
            if i==j: #comparing the data of two arrays
                counter+=1 #Increment counter for the same elements
        print (('Displacement of coincidence for'),k,(' is:'),counter)
        countCoincidences.append(counter)
        k+=1
        counter=0
    return countCoincidences
# Method to find possible keys
# Get maximum coincidences
def possible_keys(countCoincidences):
    len=max(countCoincidences)
    len1=sorted(set(countCoincidences))[-2]
    len2=sorted(set(countCoincidences))[-3]
    len3=sorted(set(countCoincidences))[-4]
    len4=sorted(set(countCoincidences))[-5]
    len5=sorted(set(countCoincidences))[-6]
    print('\n')
    print(('Highest number of coincidences are: '),len,len1,len2,len3,len4,len5)
    len=countCoincidences.index(len)
    len+=1
    len1=countCoincidences.index(len1)
    len1+=1
    len2=countCoincidences.index(len2)
    len2+=1
    len3=countCoincidences.index(len3)
    len3+=1
    len4=countCoincidences.index(len4)
    len4+=1
    len5=countCoincidences.index(len5)
    len5+=1
    lengthsArray=[len,len1,len2,len3,len4,len5]
    return lengthsArray
# Method to find the decryption key
def decryptionKeyValue(cipherText,length):
    countAlphabets=[[]for i1 in range(0,length)]
    tempVariable=0
    while tempVariable<length:
        for i2 in range(tempVariable, len(cipherText), length):
            countAlphabets[tempVariable].append(cipherText[i2])
        tempVariable += 1
    tempVariable = 0
    keyArray = []
    while tempVariable < length:
# count each alphabet
        wordCount=[]
        for character in alphabets:
            count1 = countAlphabets[tempVariable].count(character)
            count1 = count1 / 26
            count1 = round(count1, 7)
            wordCount.append(count1)
        probability_loops = 26
# Storing probability of each alphabet
        cipherProbability = []
        shifts = 0
        while probability_loops >= 0:
            shiftTemp = shift_left(probability_alpha, shifts)
            temp = np.dot(wordCount, shiftTemp)
            temp = round(temp, 6)
            cipherProbability.append(temp)
            probability_loops -= 1
            shifts += 1
        Max_probability = max(cipherProbability)
        char_num = [i for i, E in enumerate(cipherProbability) if E == Max_probability]
        char_num[0] = ((26 - char_num[0]) % 26)
        key = asciiConverter[char_num[0]].upper()
        keyArray.append(key)
        decipherCharacter = []
        for character in countAlphabets[tempVariable]:
            number = ord(character) - 97
            number = ((number - char_num[0]) % 26)
            decipherCharacter.append(number)
        final_char = []
        for i in decipherCharacter:
            final_char.append(asciiConverter[i])
        countAlphabets[tempVariable]=final_char
        tempVariable += 1
    return keyArray, countAlphabets


# decrypt ciphered text
def cipherPlainText(cipherText, length, countAlphabets):
    tempVariable = 0
    var = 0
    deciphered_text = []
    length_part = int(len(cipherText) / length)
    while var < length_part:  # Loop for storing deciphered text in each part
        while tempVariable < length:
            deciphered_text.append(countAlphabets[tempVariable][var])
            tempVariable += 1
        var += 1
        tempVariable = 0
    tempVariable = 0
    while tempVariable < (len(cipherText) % length):
        deciphered_text.append(countAlphabets[tempVariable][var])
        tempVariable += 1
    print('\n')
    print('Your plain Text:')
    print(''.join(str(elm) for elm in deciphered_text))
cipherText = "OSEBSAQBACHXBZKHWVTFNHLRQRJRNPNZRARQIQRYASYQEXZRELVIAGURPYAMCWHCNXVGHQJXGUCAMGMGWMQYCWIFFDXVRICAXURPNJBECJWVFYRHORDXVRJCVYFGBXWBZCCLVAEFIYYQJMQGMVQLCGLOVAEDTGUCMEVYWVEVYYPEVABXMGVQQEAGQCSCLMDCBHQNIPBLCMAHCMXHCNNRPRGEIORCWXUVLTMATQQIJNQRRGRPAYCGCMFLNDAIFUZXYGBDJTCYYDWRVRBEYYTNVLJCUPSBPHSHGMBMGGFNVROCRRTSSWRLGMVQLVRFSHYBMSLBSWSUNPVXBQMJPVGRUIOEYRRJBPTXBBKHYAVMWXHCNNRPRKHYAVMWMGQMNWABRYIEZGCQRGMFSEXZNJBECJQGBKVCQBWXYJNLCWBZCCLVAECLEBUWEGLMDMGVQJFFBJDXRYWNWFRLCMNYRQEGJCBLBHJMAVGFXYGQCUELZYYSHGYYPNAMOGNZNJMTAFNEEUCJVJRJUPRGQMSVGRXQZLJJMQUGBTNCCAJVAYUPLNQRHRGFNVRFQXQRGFRRTBDCLRFGVTYVARXLBDCLRGPDPLTPNEGZGWHNOMDXLBSCYCCCWGRSGAINUCJHVZJRWGRLRRTGMKITVLFMGUQJMQGSYTRAANAUNRQEIRUNXBTMDTBAYKWBYSCIYLLXXUVLPWNVBCSZZWLLRRPRPLJPXRTGSYTRAANANTENHNACWIETCCMPSGWKREUNLNICCABQGBXVAACGYHCBAUNRJVRGFNCSVPBXPYSNARXLXABACXJGUCPEATUQMGGGWKGBLHIFVBAIPBEWMMRFRQNAWFLRECQYZFYRHGBKVCQBSKXSHJUCVQMWXPNJUXUNRVYPUMOEPYSNCBHBXRGXLXAJUCAIGBJXSXSMALVZYWHVGQJFBHRJXUBSBEAQRXSARYPEVAQCCBHPAYAAGWKNTYRRFGFRQOLYLGVQCWXVZLXXFBQDVRNZ".lower()
cipherText=list(cipherText)
copyCipherText=cipherText
coincidences = calculateCoincidences(cipherText, copyCipherText)
possibleLengths = possible_keys(coincidences)
gcdValues = gcd(possibleLengths[0],possibleLengths[1])
length=gcdValues
print('\n')
print(('Key length is'),length)
print('\n')
print('Encryption Key:')
return_val = decryptionKeyValue(cipherText, length)
key = ''.join(return_val[0])
print(key)
countAlphabets = return_val[1]
cipherPlainText(cipherText, length, countAlphabets)