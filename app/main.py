from flask import Flask, render_template, request, Response
import random
import os

app = Flask(__name__)

# Updated attendee list
attendees = [
    "Avry How", "Bharath Rishivanth", 
    "Anny Zhou", "Chris Su", "Wade Cai", "Simon Liu", "Eric Zhong", 
    "Douglas Zheng", "Arnel Marquez", "Brian Gao", "Henry Nguyen/Brian Vu", 
    "Mary Li", "Ziv Lee", "Wilson Huang", "Harry Liao", 
    "Burhan/Tito Panji", "Jerome Chiu", "Chester Lee", 
    "Terry Tseng", "Chloe Poon", "Yan Cheung", "Venurse Leong", "Guo Ren", 
    "Andy Kang", "Lucas Lu", "Bill He", "Packer Chen"
]
quizzes = [
    "Scenario 1: Email Summary Generator", 
    "Scenario 2: CSV Data Cleaner", 
    "Scenario 3: Job Listings Aggregator", 
    "Scenario 4: FAQ Chatbot", 
    "Scenario 5: QR Code Generator", 
    "Scenario 6: Sentiment Analysis Tool", 
    "Scenario 7: Expense Tracker", 
    "Scenario 8: Code Quality Checker", 
    "Scenario 9: Sales Dashboard", 
    "Scenario 10: Weather Forecast API"
]

results = {}  # Store results globally for export

@app.route('/', methods=['GET', 'POST'])
def index():
    global results
    results = {}
    if request.method == 'POST':
        random.shuffle(attendees)  # Shuffle the attendees list randomly
        for i in range(len(attendees)):
            # Use modulo to ensure quizzes are assigned cyclically if attendees > quizzes
            results[i + 1] = (attendees[i], quizzes[i % len(quizzes)])  # Include line number as key
        
        print(results)  # Debugging: Print results to the console
    return render_template('index.html', results=results, quizzes=quizzes)

@app.route('/export', methods=['GET'])
def export_results():
    global results
    if not results:
        return "No results to export. Please generate the random draw first.", 400
    
    # Ensure the "log" folder exists
    log_folder = os.path.join(os.getcwd(), "log")
    os.makedirs(log_folder, exist_ok=True)
    
    # Generate the content of the .txt file
    output = "Line No. | Attendee - Quiz Mapping:\n\n"
    for line_no, (attendee, quiz) in results.items():
        output += f"{line_no}. {attendee}: {quiz}\n"
    
    # Save the log file in the "log" folder
    log_file_path = os.path.join(log_folder, "random_draw_results.txt")
    with open(log_file_path, "w") as log_file:
        log_file.write(output)
    
    # Return the log file as a downloadable response
    return Response(
        output,
        mimetype="text/plain",
        headers={"Content-Disposition": f"attachment;filename=random_draw_results.txt"}
    )

@app.route('/update_results', methods=['POST'])
def update_results():
    global results
    try:
        # 接收 JSON 格式的拖放後結果
        updated_results = request.json
        if not updated_results:
            return "Invalid data format", 400
        
        # 更新全域 results
        results = {int(k): tuple(v) for k, v in updated_results.items()}
        return "Results updated successfully", 200
    except Exception as e:
        return f"Error updating results: {str(e)}", 500

@app.route('/reassign_quiz', methods=['POST'])
def reassign_quiz():
    global results
    try:
        data = request.json
        attendee_name = data.get('attendee')
        new_quiz = data.get('quiz')

        if not attendee_name or not new_quiz:
            return "Invalid data format", 400

        # 更新指定參與者的測驗
        for line_no, (attendee, quiz) in results.items():
            if attendee == attendee_name:
                results[line_no] = (attendee, new_quiz)
                break
        else:
            return "Attendee not found", 404

        return "Attendee's quiz reassigned successfully", 200
    except Exception as e:
        return f"Error reassigning quiz: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)