import preprocess
import numpy as np

def count_words(data, y):
    result = dict()
    for y,sentence in zip(y, data):
        for word in sentence:
            pair = (word, y)
            
            if pair in result:
                result[pair] += 1
            else: result[pair] = 1

    return result 

#main method is just to verify upper methods
def main():
    data = ["ဇာတ်လမ်းကချာတယ်",
            "တကယ် ချာချက်",
            "ဇာတ်လမ်းအစမှာထဲက ကိုမကြိုက်တာ:(",
            "နောက်ဆုံးခန်းကြီးက ရုပ်ပေါက်လွန်းပါတယ်",
            "စောက်ပေါကားကြီး:/",]
    words = preprocess.segment_words(data)
    y = np.ones(len(data))
    result = count_words(words, y)
    print(result)

main()

