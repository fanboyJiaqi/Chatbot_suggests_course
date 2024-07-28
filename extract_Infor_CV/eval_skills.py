import json

label_cv1 = ["Java", "C++", "Python", "Machine Learning", "Algorithms", "Natural Language Processing",
                    "Deep Learning", "Computer Vision", "Pattern Recognition", "Data Science", "Data Analysis",
                    "Software Engineer", "Data Analyst", "C", "PySpark", "Kubeflow"]
label_cv144 = ["Electrical Circuits" ,"Circuit Breakers", "Induction Motors", "Motor Starters" , "DCADD", "AutoCAD"," Smart sheet application", "Box application", "Microsoft office 2003, 2007 & 2010 open office", "Power point "," Photo Shop"]



def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def process_labels(labels):
    # Chuyển đổi tất cả các chuỗi thành chữ thường và loại bỏ khoảng trống
    processed_labels = [label.lower().strip() for label in labels]
    return processed_labels

def eval_skill_cv(skill_cv, label_cv):
    # Extract technical skills from JSON
    label_cv = process_labels(label_cv)
    technical_skills = skill_cv['Skills']['TechnicalSkills']
    technical_skills = process_labels(technical_skills)
    count = 0
    for skill in technical_skills :
        if skill in label_cv:
            count += 1


    acc = (count/len(label_cv))*100
    return acc



skils_cv1 = read_json("label_skill_cv/skills_cv1_1.json")
print(eval_skill_cv(skils_cv1, label_cv1))

skils_cv144 = read_json("label_skill_cv/skills_cv144_2.json")
print(eval_skill_cv(skils_cv144, label_cv144))
