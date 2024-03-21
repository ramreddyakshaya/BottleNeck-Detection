from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ip1 = request.form['ip.flags.df']
    ip2 = request.form['frame.len']
    ip3 = request.form['Rx_Bytes']
    ip4 = request.form['tcp.srcport']
    ip5 = request.form['Tx_Bytes']
    ip6 = request.form['Tx_Packets']
    ip7 = request.form['Packets']
    ip8 = request.form['Rx_Packets']
    print(ip1, ip2, ip3, ip4, ip5, ip6, ip7, ip8)

    with open('voting_classifier.pkl', 'rb') as f:
        loaded_clf = pickle.load(f)

    new_data = [[ip1, ip2, ip3, ip4, ip5, ip6, ip7, ip8]]
    new_predictions = loaded_clf.predict(new_data)
    print(new_predictions)
    
    if new_predictions == [0]:
        prediction_result = 'DDoS-ACK'
        print(prediction_result)
    elif new_predictions == [1]:
        prediction_result = 'Benign'
        print(prediction_result)
    else:
        prediction_result = 'DDoS-PSH-ACK'
        print(prediction_result)
    return render_template('index.html', prediction_result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)