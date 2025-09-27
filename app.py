
import os
from flask import Flask, request, jsonify
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('API_SECRET_KEY')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        df = pd.read_csv(file)
        
        missing_values_before = df.isnull().sum().to_dict()
        
        df.drop_duplicates(inplace=True)
        
        column_to_correct = request.form.get('column_to_correct')
        if column_to_correct and column_to_correct in df.columns:
            df[column_to_correct] = pd.to_numeric(df[column_to_correct], errors='coerce')
            
        for col in df.select_dtypes(include=['number']).columns:
            df[col].fillna(df[col].mean(), inplace=True)
            
        cleaned_head = df.head().to_dict(orient='records')
        data_summary = df.describe().to_dict()

        return jsonify({
            'message': 'File processed successfully',
            'original_missing_values': missing_values_before,
            'cleaned_data_head': cleaned_head,
            'data_summary': data_summary
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
