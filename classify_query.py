# classify_query.py

def classify_query(user_input):
    if "attendance" in user_input.lower():
        return "attendance"
    elif "performance" in user_input.lower() or "score" in user_input.lower():
        return "performance"
    elif "cgpa" in user_input.lower():
        return "cgpa"
    elif "student" in user_input.lower():
        return "student_info"
    else:
        return "general"
