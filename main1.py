import text_classifier
import tokenize
res_data = pd.DataFrame(pd.read_csv('final_sentence_classification_data.csv'))
your_problem_child = input("Please enter the exact problem you are facing")
text_classifier.classify(tokenize.tokenizer(res_data['Responses']))