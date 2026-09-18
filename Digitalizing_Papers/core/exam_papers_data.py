"""
Verified high-fidelity handwritten exam paper transcripts and structured sections
for Swami Pradeep Public School.
Covers:
- KG-1 Math (paper 1.pdf)
- Class 3 Maths (paper 2.pdf)
- Class 4 Maths (paper 3.pdf)
- Class 5 Maths (Adobe Scan 18 Sept 2026.pdf)
- Class 6 Maths (Adobe Scan 18 Sept 2026 (1).pdf)
- Class 7 Maths (paper 7.pdf)
- Class 8 Maths (Adobe Scan 18 Sept 2026 (2).pdf)
"""

from typing import Tuple, Dict, Any

def get_paper_kg1_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """Swami Pradeep Public School
Class - Kg 1
Subject - Math
त्रैमासिक परीक्षा (Quarterly Examination 2026-27)
पूर्णांक: 50 | समय: 2.0 घंटे

प्रश्न 1. गिनकर संख्या लिखो (10 अंक)
1. 🍎 🍎  —  ______
2. ⭐ ⭐ ⭐  —  ______
3. 🌸 🌸 🌸 🌸  —  ______
4. ⭕  —  ______
5. 🔺 🔺 🔺 🔺 🔺  —  ______

प्रश्न 2. खाली स्थान भरो (10 अंक)
1. 1, _____ , 3
2. 3, _____ , 5
3. 5, _____ , 7
4. 7, _____ , 9
5. 10, _____ , 12

प्रश्न 3. 1 से 10 तक गिनती लिखो (10 अंक)
1 to 10 Counting

प्रश्न 4. सही संख्या पर गोला (O) लगाओ (10 अंक)
1. 🍎 🍎  ->  1 / 2 / 3
2. 🌷 🌷 🌷  ->  3 / 1 / 2
3. 🐟 🐟 🐟 🐟  ->  4 / 5 / 6
4. 🥭 🥭 🥭 🥭 🥭  ->  5 / 2 / 3
5. 🌸 🌸  ->  2 / 1 / 6

प्रश्न 5. सही संख्या से मिलान कीजिए (10 अंक)
1. 2  —  ⌛ (1)
2. 1  —  🐟 🐟 🐟 (3)
3. 3  —  ⭐ ⭐ ⭐ ⭐ ⭐ (5)
4. 5  —  🔺 🔺 🔺 🔺 (4)
5. 4  —  🌳 🌳 (2)
"""
    structured = {
        "metadata": {
            "class_name": "Class_KG1",
            "subject": "Mathematics",
            "exam_type": "Quarterly",
            "time_allowed": "2.0 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "सभी प्रश्न अनिवार्य हैं।",
            "उत्तर सुंदर एवं स्पष्ट अक्षरों में लिखें।"
        ],
        "sections": [
            {
                "title": "प्रश्न 1. गिनकर संख्या लिखो (Count & Write)",
                "questions": [
                    {"number": "1.", "text": "🍎 🍎 &nbsp;&nbsp;&mdash;&nbsp;&nbsp; [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]", "marks": "2", "is_or_choice": False},
                    {"number": "2.", "text": "⭐ ⭐ ⭐ &nbsp;&nbsp;&mdash;&nbsp;&nbsp; [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]", "marks": "2", "is_or_choice": False},
                    {"number": "3.", "text": "🌸 🌸 🌸 🌸 &nbsp;&nbsp;&mdash;&nbsp;&nbsp; [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]", "marks": "2", "is_or_choice": False},
                    {"number": "4.", "text": "⭕ &nbsp;&nbsp;&mdash;&nbsp;&nbsp; [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]", "marks": "2", "is_or_choice": False},
                    {"number": "5.", "text": "🔺 🔺 🔺 🔺 🔺 &nbsp;&nbsp;&mdash;&nbsp;&nbsp; [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]", "marks": "2", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 2. खाली स्थान भरो (Fill in the blanks)",
                "questions": [
                    {"number": "1.", "text": "1 , &nbsp;&nbsp; ______ , &nbsp;&nbsp; 3", "marks": "2", "is_or_choice": False},
                    {"number": "2.", "text": "3 , &nbsp;&nbsp; ______ , &nbsp;&nbsp; 5", "marks": "2", "is_or_choice": False},
                    {"number": "3.", "text": "5 , &nbsp;&nbsp; ______ , &nbsp;&nbsp; 7", "marks": "2", "is_or_choice": False},
                    {"number": "4.", "text": "7 , &nbsp;&nbsp; ______ , &nbsp;&nbsp; 9", "marks": "2", "is_or_choice": False},
                    {"number": "5.", "text": "10 , &nbsp;&nbsp; ______ , &nbsp;&nbsp; 12", "marks": "2", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 3. गिनती (Counting 1 to 10)",
                "questions": [
                    {"number": "1.", "text": "1 से 10 तक गिनती (1 to 10 Counting) सुंदर अक्षरों में लिखिए:<br/><br/><table style='width: 100%; border-collapse: collapse; text-align: center;' border='1'><tr><td style='padding: 12px; width: 10%; font-weight: bold;'>1</td><td style='padding: 12px; width: 10%;'>&nbsp;</td><td style='padding: 12px; width: 10%;'>&nbsp;</td><td style='padding: 12px; width: 10%;'>&nbsp;</td><td style='padding: 12px; width: 10%;'>&nbsp;</td><td style='padding: 12px; width: 10%;'>&nbsp;</td><td style='padding: 12px; width: 10%;'>&nbsp;</td><td style='padding: 12px; width: 10%;'>&nbsp;</td><td style='padding: 12px; width: 10%;'>&nbsp;</td><td style='padding: 12px; width: 10%; font-weight: bold;'>10</td></tr></table>", "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 4. सही संख्या पर गोला (O) लगाओ (Circle the Correct Number)",
                "questions": [
                    {"number": "1.", "text": "🍎 🍎 &nbsp;&nbsp;&rarr;&nbsp;&nbsp; <b>1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3</b>", "marks": "2", "is_or_choice": False},
                    {"number": "2.", "text": "🌷 🌷 🌷 &nbsp;&nbsp;&rarr;&nbsp;&nbsp; <b>3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2</b>", "marks": "2", "is_or_choice": False},
                    {"number": "3.", "text": "🐟 🐟 🐟 🐟 &nbsp;&nbsp;&rarr;&nbsp;&nbsp; <b>4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6</b>", "marks": "2", "is_or_choice": False},
                    {"number": "4.", "text": "🥭 🥭 🥭 🥭 🥭 &nbsp;&nbsp;&rarr;&nbsp;&nbsp; <b>5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3</b>", "marks": "2", "is_or_choice": False},
                    {"number": "5.", "text": "🌸 🌸 &nbsp;&nbsp;&rarr;&nbsp;&nbsp; <b>2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6</b>", "marks": "2", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 5. सही संख्या से मिलान कीजिए (Match the following)",
                "questions": [
                    {"number": "1.", "text": "2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⌛ (1)", "marks": "2", "is_or_choice": False},
                    {"number": "2.", "text": "1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🐟 🐟 🐟 (3)", "marks": "2", "is_or_choice": False},
                    {"number": "3.", "text": "3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⭐ ⭐ ⭐ ⭐ ⭐ (5)", "marks": "2", "is_or_choice": False},
                    {"number": "4.", "text": "5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🔺 🔺 🔺 🔺 (4)", "marks": "2", "is_or_choice": False},
                    {"number": "5.", "text": "4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🌳 🌳 (2)", "marks": "2", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


def get_paper_class3_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """Swami Pradeep Public School
Class - 3rd
Subject - Maths
Quarterly Examination (त्रैमासिक परीक्षा 2026-27)
पूर्णांक: 50 | समय: 2.5 घंटे

1. Write the number names (10 no.)
1. 659 - ____________________________________
2. 2222 - ____________________________________
3. 1800 - ____________________________________
4. 999 - ____________________________________
5. 3890 - ____________________________________

2. Fill in the blanks using >, < or = : (5 no.)
i   64 [   ] 46
ii  770 [   ] 170
iii 1000 [   ] 0001
iv  999 [   ] 9899
v   198 [   ] 891

3. Write the place value of the underlined digit: (5 no.)
1. 682  (8 is underlined)
2. 4780 (7 is underlined)
3. 540  (0 is underlined)
4. 8760 (8 is underlined)
5. 7999 (first 9 is underlined)

4. Write the greatest and smallest digit number formed by using the digits: (5 no.)
1. 6, 1, 2
2. 7, 4, 8, 3
3. 9, 7, 0
4. 9, 8, 6
5. 7, 6, 5, 4

5. Add: (10 no.)
(a) 5432 + 2425
(b) 3476 + 2534
(c) 1634 + 8285
(d) 4713 + 3692
(e) 8463 + 4359

6. Subtract: (10 no.)
(a) 9567 - 1235
(b) 2768 - 1435
(c) 8459 - 5234
(d) 9453 - 0124
(e) 7854 - 5630

7. Multiplication: (5 no.)
(a) 266 x 2
(b) 4262 x 4
"""
    structured = {
        "metadata": {
            "class_name": "Class_3",
            "subject": "Mathematics",
            "exam_type": "Quarterly",
            "time_allowed": "2.5 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "All questions are compulsory.",
            "Write your answers neatly and show necessary working steps."
        ],
        "sections": [
            {
                "title": "Section 1: Number Names",
                "questions": [
                    {"number": "1.", "text": "Write the number names for the following:<br/>"
                                              "(a) <b>659</b> &nbsp;&mdash;&nbsp; __________________________________________________<br/>"
                                              "(b) <b>2222</b> &nbsp;&mdash;&nbsp; __________________________________________________<br/>"
                                              "(c) <b>1800</b> &nbsp;&mdash;&nbsp; __________________________________________________<br/>"
                                              "(d) <b>999</b> &nbsp;&mdash;&nbsp; __________________________________________________<br/>"
                                              "(e) <b>3890</b> &nbsp;&mdash;&nbsp; __________________________________________________",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Section 2: Comparison of Numbers",
                "questions": [
                    {"number": "2.", "text": "Fill in the blanks using &gt;, &lt; or = :<br/>"
                                              "(i) 64 &nbsp; [ &nbsp;&nbsp;&nbsp;&nbsp; ] &nbsp; 46 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                                              "(ii) 770 &nbsp; [ &nbsp;&nbsp;&nbsp;&nbsp; ] &nbsp; 170<br/>"
                                              "(iii) 1000 &nbsp; [ &nbsp;&nbsp;&nbsp;&nbsp; ] &nbsp; 0001 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                                              "(iv) 999 &nbsp; [ &nbsp;&nbsp;&nbsp;&nbsp; ] &nbsp; 9899<br/>"
                                              "(v) 198 &nbsp; [ &nbsp;&nbsp;&nbsp;&nbsp; ] &nbsp; 891",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Section 3: Place Value",
                "questions": [
                    {"number": "3.", "text": "Write the place value of the underlined digit:<br/>"
                                              "(a) 6<u>8</u>2 &nbsp;&mdash;&nbsp; _______________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                                              "(b) 4<u>7</u>80 &nbsp;&mdash;&nbsp; _______________<br/>"
                                              "(c) 54<u>0</u> &nbsp;&mdash;&nbsp; _______________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                                              "(d) <u>8</u>760 &nbsp;&mdash;&nbsp; _______________<br/>"
                                              "(e) 7<u>9</u>99 &nbsp;&mdash;&nbsp; _______________",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Section 4: Number Formation",
                "questions": [
                    {"number": "4.", "text": "Write the greatest and smallest number formed by using the given digits:<br/><br/>"
                                              "<table style='width: 100%; border-collapse: collapse; text-align: center;' border='1'>"
                                              "<tr style='background: #f0f4f8;'><th>S.No.</th><th>Digits</th><th>Greatest Number</th><th>Smallest Number</th></tr>"
                                              "<tr><td>1</td><td>6, 1, 2</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
                                              "<tr><td>2</td><td>7, 4, 8, 3</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
                                              "<tr><td>3</td><td>9, 7, 0</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
                                              "<tr><td>4</td><td>9, 8, 6</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
                                              "<tr><td>5</td><td>7, 6, 5, 4</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
                                              "</table>",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Section 5: Addition",
                "questions": [
                    {"number": "5.", "text": "Add the following numbers:<br/><br/>"
                                              "<table style='width: 100%; border-collapse: collapse; text-align: center;'>"
                                              "<tr>"
                                              "<td style='padding: 8px;'><b>(a)</b><br/>Th H T O<br/>&nbsp;&nbsp;5 4 3 2<br/>+ 2 4 2 5<br/>-----------</td>"
                                              "<td style='padding: 8px;'><b>(b)</b><br/>Th H T O<br/>&nbsp;&nbsp;3 4 7 6<br/>+ 2 5 3 4<br/>-----------</td>"
                                              "<td style='padding: 8px;'><b>(c)</b><br/>Th H T O<br/>&nbsp;&nbsp;1 6 3 4<br/>+ 8 2 8 5<br/>-----------</td>"
                                              "</tr><tr>"
                                              "<td style='padding: 8px;'><b>(d)</b><br/>Th H T O<br/>&nbsp;&nbsp;4 7 1 3<br/>+ 3 6 9 2<br/>-----------</td>"
                                              "<td style='padding: 8px;' colspan='2'><b>(e)</b><br/>Th H T O<br/>&nbsp;&nbsp;8 4 6 3<br/>+ 4 3 5 9<br/>-----------</td>"
                                              "</tr></table>",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Section 6: Subtraction",
                "questions": [
                    {"number": "6.", "text": "Subtract the following numbers:<br/><br/>"
                                              "<table style='width: 100%; border-collapse: collapse; text-align: center;'>"
                                              "<tr>"
                                              "<td style='padding: 8px;'><b>(a)</b><br/>Th H T O<br/>&nbsp;&nbsp;9 5 6 7<br/>- 1 2 3 5<br/>-----------</td>"
                                              "<td style='padding: 8px;'><b>(b)</b><br/>Th H T O<br/>&nbsp;&nbsp;2 7 6 8<br/>- 1 4 3 5<br/>-----------</td>"
                                              "<td style='padding: 8px;'><b>(c)</b><br/>Th H T O<br/>&nbsp;&nbsp;8 4 5 9<br/>- 5 2 3 4<br/>-----------</td>"
                                              "</tr><tr>"
                                              "<td style='padding: 8px;'><b>(d)</b><br/>Th H T O<br/>&nbsp;&nbsp;9 4 5 3<br/>- 0 1 2 4<br/>-----------</td>"
                                              "<td style='padding: 8px;' colspan='2'><b>(e)</b><br/>Th H T O<br/>&nbsp;&nbsp;7 8 5 4<br/>- 5 6 3 0<br/>-----------</td>"
                                              "</tr></table>",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Section 7: Multiplication",
                "questions": [
                    {"number": "7.", "text": "Multiply the following:<br/><br/>"
                                              "<table style='width: 70%; margin: 0 auto; border-collapse: collapse; text-align: center;'>"
                                              "<tr>"
                                              "<td style='padding: 8px;'><b>(a)</b><br/>H T O<br/>&nbsp;&nbsp;2 6 6<br/>&times;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2<br/>-------</td>"
                                              "<td style='padding: 8px;'><b>(b)</b><br/>Th H T O<br/>&nbsp;&nbsp;4 2 6 2<br/>&times;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4<br/>---------</td>"
                                              "</tr></table>",
                     "marks": "5", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


def get_paper_class4_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """Swami Pradeep Public School
Class - 4th
Subject - Maths
त्रैमासिक परीक्षा (Quarterly Examination 2026-27)
पूर्णांक: 50 | समय: 2.5 घंटे

1. रिक्त स्थानों को भरिए (5 अंक)
1. जिस फलक पर 2 लिखा है उसके विपरीत फलक पर _________ है।
2. जिस फलक पर 4 लिखा है उसके विपरीत फलक पर _________ है।
3. मेरे 6 फलक, 12 किनारे और 8 कोने हैं, मैं _________ हूँ।
4. जब हम पंचभुज आकृति को सरकाते हैं तो आकृति में _________ परिवर्तन होता है।
5. व्यास की लंबाई त्रिज्या की लंबाई की _________ होती है।

2. समकोण, न्यून कोण, अधिक कोण बनाइए (10 अंक)

3. अपनी कक्षा में विद्यमान ऐसी वस्तुओं के नाम बताइए जिनमें न्यून कोण है। (5 अंक)

4. अपनी कक्षा में विद्यमान कुछ ऐसी वस्तुओं के नाम बताइए जिनमें अधिक कोण है। (5 अंक)

5. नि.लि. अक्षरों में स्थित सभी कोणों की पहचान कीजिए: (10 अंक)
Letters: V, A, Z

6. सम संख्याएँ और विषम संख्याएँ अलग-अलग छाँटकर लिखिए: (5 अंक)
96, 24, 17, 04, 85, 76, 17, 74, 52, 99, 74, 84, 18, 19, 29, 30, 77, 99

7. नि.लि. की परिभाषाएं लिखिए तथा चित्र बनाइए: (10 अंक)
वर्ग, त्रिभुज, आयत, घनाभ, घन
"""
    structured = {
        "metadata": {
            "class_name": "Class_4",
            "subject": "Mathematics",
            "exam_type": "Quarterly",
            "time_allowed": "2.5 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "सभी प्रश्न अनिवार्य हैं।",
            "जहाँ आवश्यक हो वहाँ स्वच्छ एवं स्पष्ट ज्यामितीय चित्र बनाइए।"
        ],
        "sections": [
            {
                "title": "प्रश्न 1. रिक्त स्थानों की पूर्ति कीजिए",
                "questions": [
                    {"number": "1.", "text": "जिस फलक पर 2 लिखा है उसके ठीक विपरीत फलक पर __________________ संख्या होती है।", "marks": "1", "is_or_choice": False},
                    {"number": "2.", "text": "जिस फलक पर 4 लिखा है उसके ठीक विपरीत फलक पर __________________ संख्या होती है।", "marks": "1", "is_or_choice": False},
                    {"number": "3.", "text": "मेरे 6 फलक, 12 किनारे और 8 कोने हैं, मेरी आकृति __________________ है।", "marks": "1", "is_or_choice": False},
                    {"number": "4.", "text": "जब हम पंचभुज आकृति को सरकाते हैं तो उसकी आकृति में __________________ परिवर्तन होता है।", "marks": "1", "is_or_choice": False},
                    {"number": "5.", "text": "वृत्त के व्यास की लंबाई उसकी त्रिज्या की लंबाई की __________________ होती है।", "marks": "1", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 2. कोणों का निर्माण",
                "questions": [
                    {"number": "6.", "text": "समकोण (Right Angle), न्यून कोण (Acute Angle) तथा अधिक कोण (Obtuse Angle) का स्वच्छ नामांकित चित्र बनाइए एवं उनका माप लिखिए।", "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 3 एवं 4. परिवेश में कोणों की पहचान",
                "questions": [
                    {"number": "7.", "text": "अपनी कक्षा में विद्यमान ऐसी किन्हीं 5 वस्तुओं के नाम बताइए जिनमें न्यून कोण बनता है।", "marks": "5", "is_or_choice": False},
                    {"number": "8.", "text": "अपनी कक्षा में विद्यमान कुछ ऐसी वस्तुओं के नाम बताइए जिनमें अधिक कोण बनता है।", "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 5. अक्षरों में स्थित कोण",
                "questions": [
                    {"number": "9.", "text": "निम्नलिखित अंग्रेजी वर्णमाला के अक्षरों में स्थित सभी कोणों (न्यून कोण, अधिक कोण अथवा समकोण) की पहचान कर उनकी संख्या लिखिए:<br/><br/>"
                                              "<div style='font-size: 26px; font-weight: bold; letter-spacing: 40px; text-align: center; margin: 10px 0;'>V &nbsp;&nbsp;&nbsp;&nbsp; A &nbsp;&nbsp;&nbsp;&nbsp; Z</div>",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 6. सम एवं विषम संख्याएँ",
                "questions": [
                    {"number": "10.", "text": "नीचे दी गई संख्याओं में से <b>सम संख्याएँ</b> और <b>विषम संख्याएँ</b> अलग-अलग छाँटकर तालिका में लिखिए:<br/>"
                                               "<p style='background: #f7fafc; padding: 8px; border: 1px dashed #cbd5e0; font-size: 13px; text-align: center;'>"
                                               "<b>96, &nbsp; 24, &nbsp; 17, &nbsp; 04, &nbsp; 85, &nbsp; 76, &nbsp; 17, &nbsp; 74, &nbsp; 52, &nbsp; 99, &nbsp; 74, &nbsp; 84, &nbsp; 18, &nbsp; 19, &nbsp; 29, &nbsp; 30, &nbsp; 77, &nbsp; 99</b></p>",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 7. ज्यामितीय परिभाषाएं एवं चित्र",
                "questions": [
                    {"number": "11.", "text": "निम्नलिखित ज्यामितीय आकृतियों की परिभाषा लिखिए तथा उनका स्वच्छ चित्र बनाइए:<br/>"
                                               "(क) वर्ग (Square)<br/>"
                                               "(ख) त्रिभुज (Triangle)<br/>"
                                               "(ग) आयत (Rectangle)<br/>"
                                               "(घ) घनाभ (Cuboid)<br/>"
                                               "(ङ) घन (Cube)",
                     "marks": "10", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


def get_paper_class5_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """स्वामी प्रदीप पब्लिक स्कूल देवरी सागर (म.प्र.)
विषय - गणित
कक्षा - 5वीं
त्रैमासिक परीक्षा सत्र 2026-27
पूर्णांक: 50 | समय: 2.5 घंटे

प्रश्न 1] सही विकल्प चुनिए: (5 अंक)
1] तीन भुजाओं से बनी बंद आकृति को कहते हैं:
   (a) आयत  (b) त्रिभुज  (c) वर्ग
2] त्रिभुज के तीनों कोणों का योग होता है:
   (a) 90°  (b) 180°  (c) 60°
3] पंचभुज कितनी भुजाओं वाली बंद आकृति है:
   (a) 3  (b) 6  (c) 5
4] 8 x 6 का हल होगा:
   (a) 40  (b) 48  (c) 56
5] एक चौथाई को व्यक्त करते हैं:
   (a) 1/2  (b) 1/4  (c) 1/8

प्रश्न 2] सत्य / असत्य लिखिए: (5 अंक)
1] आयत का परिमाप 2 x (लंबाई + चौड़ाई) होता है।
2] जिसकी सभी भुजाएं बराबर होती हैं आयत कहलाता है।
3] 50 पैसे एक रुपये का आधा होता है।
4] 1 घंटे में 120 मिनट होते हैं।
5] 4 x 4 का हल 16 है।

प्रश्न 3] रिक्त स्थान भरिए: (5 अंक)
1] समकोण का आधा _________ होता है।
2] समकोण का दोगुना _________ होता है।
3] एक वर्ग की भुजा 8 सेमी है तो उसका क्षेत्रफल _________ होगा।
4] दो अंकों की सबसे बड़ी संख्या _________ है।
5] △ (त्रिभुज) को आधा घुमाने पर _________ प्राप्त होगा।

प्रश्न 4] आकृतियों व अक्षरों का घूर्णन (6 अंक)
1] अंग्रेजी वर्णमाला में ऐसे कौन-से अक्षर हैं जिन्हें आधा घुमाने पर वैसे ही दिखते हैं?
2] 0 से 9 तक के अंकों को आधा घुमाओ, इनमें से कौन से अंक पहले जैसे दिखाई देते हैं?

प्रश्न 5] व्यावहारिक गणितीय समस्याएं (10 अंक)
1] तुम्हारी तरह के 12 बच्चों का कुल वजन कितना होगा?
2] फाजिला ने बड़ी मछली किंगफिश को 1200 रु. में बेचा। 8 कि.ग्रा. मछली 1200 रु. की है तो एक कि.ग्रा. मछली कितने में बेचेंगी?
3] एक वर्ग की भुजा 4 सेमी. है, वर्ग का क्षेत्रफल ज्ञात कीजिए?

प्रश्न 6] परिभाषाएं, ज्यामिति व गुणन (11 अंक)
1] त्रिभुज की परिभाषा लिखिए।
2] गुणा कीजिए:
   1] 78 x 52    2] 65 x 34    3] 92 x 35
   4] 58 x 26    5] 66 x 37    6] 58 x 17
3] तीन भुजाओं वाली 2 बंद आकृति तथा 2 खुली आकृति बनाइए।

प्रश्न 7] समकोण एवं मूल्य तालिका (खरीदारी सूची) (8 अंक)
1] समकोण किसे कहते हैं?
2] कीर्ति की खरीदारी सूची देखो और नीचे दिए गए प्रश्नों के उत्तर दो:
   टमाटर: 12 रु/किग्रा | आलू: 10 रु/किग्रा | प्याज: 16 रु/किग्रा | गाजर: 18 रु/किग्रा | लौकी: 8 रु/किग्रा
   (i) दो किलो टमाटर कितने के हैं?
   (ii) 5 किलो आलू कितने के हैं?
   (iii) 1/2 किलो टमाटर कितने के हैं?
   (iv) 3 किलो गाजर कितनी है?
   (v) 4 किलो लौकी कितने की हैं?
"""
    structured = {
        "metadata": {
            "class_name": "Class_5",
            "subject": "Mathematics",
            "exam_type": "Quarterly",
            "time_allowed": "2.5 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "सभी प्रश्न हल करना अनिवार्य है।",
            "गणना एवं उत्तर स्वच्छ हस्तलेख में लिखें।"
        ],
        "sections": [
            {
                "title": "खंड - 'क' : वस्तुनिष्ठ प्रश्न (MCQ)",
                "questions": [
                    {"number": "1.", "text": "तीन भुजाओं से बनी बंद आकृति को कहते हैं:<br/>(a) आयत &nbsp;&nbsp;&nbsp;&nbsp; (b) त्रिभुज &nbsp;&nbsp;&nbsp;&nbsp; (c) वर्ग", "marks": "1", "is_or_choice": False},
                    {"number": "2.", "text": "त्रिभुज के तीनों अंतःकोणों का योग होता है:<br/>(a) 90&deg; &nbsp;&nbsp;&nbsp;&nbsp; (b) 180&deg; &nbsp;&nbsp;&nbsp;&nbsp; (c) 60&deg;", "marks": "1", "is_or_choice": False},
                    {"number": "3.", "text": "पंचभुज कितनी भुजाओं वाली बंद आकृति है?<br/>(a) 3 &nbsp;&nbsp;&nbsp;&nbsp; (b) 6 &nbsp;&nbsp;&nbsp;&nbsp; (c) 5", "marks": "1", "is_or_choice": False},
                    {"number": "4.", "text": "8 &times; 6 का गुणनफल होगा:<br/>(a) 40 &nbsp;&nbsp;&nbsp;&nbsp; (b) 48 &nbsp;&nbsp;&nbsp;&nbsp; (c) 56", "marks": "1", "is_or_choice": False},
                    {"number": "5.", "text": "एक चौथाई को भिन्न रूप में व्यक्त करते हैं:<br/>(a) 1/2 &nbsp;&nbsp;&nbsp;&nbsp; (b) 1/4 &nbsp;&nbsp;&nbsp;&nbsp; (c) 1/8", "marks": "1", "is_or_choice": False}
                ]
            },
            {
                "title": "खंड - 'ख' : सत्य / असत्य एवं रिक्त स्थान",
                "questions": [
                    {"number": "6.", "text": "सत्य अथवा असत्य लिखिए:<br/>"
                                              "(i) आयत का परिमाप = 2 &times; (लंबाई + चौड़ाई) होता है। [ &nbsp;&nbsp;&nbsp;&nbsp; ]<br/>"
                                              "(ii) जिसकी सभी भुजाएं बराबर होती हैं वह आयत कहलाता है। [ &nbsp;&nbsp;&nbsp;&nbsp; ]<br/>"
                                              "(iii) 50 पैसे एक रुपये का आधा होता है। [ &nbsp;&nbsp;&nbsp;&nbsp; ]<br/>"
                                              "(iv) 1 घंटे में 120 मिनट होते हैं। [ &nbsp;&nbsp;&nbsp;&nbsp; ]<br/>"
                                              "(v) 4 &times; 4 का हल 16 है। [ &nbsp;&nbsp;&nbsp;&nbsp; ]",
                     "marks": "5", "is_or_choice": False},
                    {"number": "7.", "text": "रिक्त स्थानों की पूर्ति कीजिए:<br/>"
                                              "(i) समकोण का आधा __________________ होता है।<br/>"
                                              "(ii) समकोण का दोगुना __________________ होता है।<br/>"
                                              "(iii) एक वर्ग की भुजा 8 सेमी है, तो उसका क्षेत्रफल __________________ होगा।<br/>"
                                              "(iv) दो अंकों की सबसे बड़ी संख्या __________________ है।<br/>"
                                              "(v) &Delta; (त्रिभुज) को आधा घुमाने पर __________________ आकृति प्राप्त होगी।",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "खंड - 'ग' : आकृतियों एवं अक्षरों का घूर्णन",
                "questions": [
                    {"number": "8.", "text": "अंग्रेजी वर्णमाला में ऐसे कौन-से अक्षर हैं जिन्हें आधा घुमाने पर वे वैसे ही दिखते हैं? उदाहरण सहित लिखिए।", "marks": "3", "is_or_choice": False},
                    {"number": "9.", "text": "0 से 9 तक के अंकों को आधा घुमाइए। इनमें से कौन-से अंक पहले जैसे ही दिखाई देते हैं?", "marks": "3", "is_or_choice": False}
                ]
            },
            {
                "title": "खंड - 'घ' : व्यावहारिक व ज्यामितीय प्रश्न",
                "questions": [
                    {"number": "10.", "text": "यदि आपके एक सहपाठी का वजन लगभग 30 किग्रा है, तो तुम्हारी तरह के 12 बच्चों का कुल अनुमानित वजन कितना होगा?", "marks": "3", "is_or_choice": False},
                    {"number": "11.", "text": "फाजिला ने एक बड़ी किंगफिश मछली को 1200 रुपये में बेचा। यदि 8 कि.ग्रा. मछली 1200 रुपये की है, तो 1 कि.ग्रा. मछली का मूल्य ज्ञात कीजिए।", "marks": "4", "is_or_choice": False},
                    {"number": "12.", "text": "एक वर्ग की भुजा 4 सेमी है। उस वर्ग का क्षेत्रफल सूत्र लिखकर ज्ञात कीजिए।", "marks": "3", "is_or_choice": False},
                    {"number": "13.", "text": "त्रिभुज की परिभाषा लिखिए तथा तीन भुजाओं वाली 2 बंद आकृतियाँ एवं 2 खुली आकृतियाँ बनाइए।", "marks": "4", "is_or_choice": False}
                ]
            },
            {
                "title": "खंड - 'ङ' : गुणन एवं तालिका आधारित प्रश्न",
                "questions": [
                    {"number": "14.", "text": "गुणा कीजिए:<br/>"
                                               "(i) 78 &times; 52 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) 65 &times; 34 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iii) 92 &times; 35<br/>"
                                               "(iv) 58 &times; 26 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (v) 66 &times; 37 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (vi) 58 &times; 17",
                     "marks": "6", "is_or_choice": False},
                    {"number": "15.", "text": "समकोण किसे कहते हैं? इसका माप कितना होता है?", "marks": "2", "is_or_choice": False},
                    {"number": "16.", "text": "कीर्ति की खरीदारी सूची देखकर निम्नलिखित प्रश्नों के उत्तर दीजिए:<br/><br/>"
                                               "<table style='width: 75%; border-collapse: collapse; text-align: center;' border='1'>"
                                               "<tr style='background: #edf2f7;'><th>सब्जी (चीज)</th><th>कीमत (रुपये प्रति किग्रा)</th></tr>"
                                               "<tr><td>टमाटर</td><td>12 रु.</td></tr>"
                                               "<tr><td>आलू</td><td>10 रु.</td></tr>"
                                               "<tr><td>प्याज</td><td>16 रु.</td></tr>"
                                               "<tr><td>गाजर</td><td>18 रु.</td></tr>"
                                               "<tr><td>लौकी</td><td>8 रु.</td></tr>"
                                               "</table><br/>"
                                               "(i) 2 किलो टमाटर की कीमत कितनी होगी?<br/>"
                                               "(ii) 5 किलो आलू की कीमत कितनी होगी?<br/>"
                                               "(iii) 1/2 किलो टमाटर कितने रुपये के होंगे?<br/>"
                                               "(iv) 3 किलो गाजर की कुल कीमत कितनी है?<br/>"
                                               "(v) 4 किलो लौकी का मूल्य ज्ञात कीजिए।",
                     "marks": "5", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


def get_paper_class6_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """त्रैमासिक परीक्षा सत्र 2026-27
विषय - गणित
कक्षा - 6वीं
पूर्णांक: 50 | समय: 2.5 घंटे

प्रश्न 1] रिक्त स्थानों को भरिए: (5 अंक)
1] 1 लाख = _________ दस हजार।
2] 1 करोड़ = _________ दस लाख।
3] 1 किलोग्राम = _________ ग्राम।
4] 1000 मीटर = _________ किलोमीटर।
5] 1 घंटा = _________ मिनट।

प्रश्न 2] निम्नलिखित संख्याओं को आरोही क्रम में लिखिए: (5 अंक)
1] 847, 9754, 8320, 571
2] 9801, 25751, 36501, 38802
3] 5000, 7500, 85400, 7861
4] 1971, 4521, 8871, 9254
5] 1473, 8944, 100, 310, 5000

प्रश्न 3] निम्न को संख्याओं (अंकों) में लिखिए: (10 अंक)
1] तिहत्तर लाख पचहत्तर हजार तीन सौ सात।
2] नौ करोड़ पांच लाख इकतालीस।
3] तेरह लाख तीस हजार दस।
4] सात हजार तीन सौ बावन।
5] सात करोड़ बावन लाख इक्कीस हजार तीन सौ दो।

प्रश्न 4] निम्न को शब्दों में लिखिए: (10 अंक)
1] 8,75,95,762
2] 85,46,228
3] 9,84,32,701
4] 74,52,283
5] 4,80,498

प्रश्न 5] निम्न के परवर्ती लिखिए: (5 अंक)
1] 24,40,701
2] 1,00,199
3] 23,45,670
4] 1,00,999
5] 9,999

प्रश्न 6] निम्न के पूर्ववर्ती लिखिए: (5 अंक)
1] 94
2] 1,000
3] 2,08,090
4] 7,654
5] 3,211

प्रश्न 7] निम्न संख्याओं के सभी गुणनखंड लिखिए: (10 अंक)
1] 24
2] 15
3] 27
4] 18
5] 36
"""
    structured = {
        "metadata": {
            "class_name": "Class_6",
            "subject": "Mathematics",
            "exam_type": "Quarterly",
            "time_allowed": "2.5 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "सभी प्रश्न अनिवार्य हैं।",
            "उत्तर पुस्तिका में प्रत्येक प्रश्न का क्रमांक स्पष्ट लिखें।"
        ],
        "sections": [
            {
                "title": "प्रश्न 1] रिक्त स्थानों की पूर्ति कीजिए",
                "questions": [
                    {"number": "1.", "text": "1 लाख = __________________ दस हजार।", "marks": "1", "is_or_choice": False},
                    {"number": "2.", "text": "1 करोड़ = __________________ दस लाख।", "marks": "1", "is_or_choice": False},
                    {"number": "3.", "text": "1 किलोग्राम = __________________ ग्राम।", "marks": "1", "is_or_choice": False},
                    {"number": "4.", "text": "1000 मीटर = __________________ किलोमीटर।", "marks": "1", "is_or_choice": False},
                    {"number": "5.", "text": "1 घंटा = __________________ मिनट।", "marks": "1", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 2] संख्याओं को आरोही क्रम (Ascending Order) में लिखिए",
                "questions": [
                    {"number": "6.", "text": "(i) 847, &nbsp; 9754, &nbsp; 8320, &nbsp; 571<br/>"
                                              "(ii) 9801, &nbsp; 25751, &nbsp; 36501, &nbsp; 38802<br/>"
                                              "(iii) 5000, &nbsp; 7500, &nbsp; 85400, &nbsp; 7861<br/>"
                                              "(iv) 1971, &nbsp; 4521, &nbsp; 8871, &nbsp; 9254<br/>"
                                              "(v) 1473, &nbsp; 8944, &nbsp; 100, &nbsp; 310, &nbsp; 5000",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 3] निम्न को संख्याओं (अंकों में) लिखिए",
                "questions": [
                    {"number": "7.", "text": "(i) तिहत्तर लाख पचहत्तर हजार तीन सौ सात।<br/>"
                                              "(ii) नौ करोड़ पांच लाख इकतालीस।<br/>"
                                              "(iii) तेरह लाख तीस हजार दस।<br/>"
                                              "(iv) सात हजार तीन सौ बावन।<br/>"
                                              "(v) सात करोड़ बावन लाख इक्कीस हजार तीन सौ दो।",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 4] निम्न संख्याओं को शब्दों में लिखिए",
                "questions": [
                    {"number": "8.", "text": "(i) 8,75,95,762 &nbsp;&mdash;&nbsp; __________________________________________________<br/>"
                                              "(ii) 85,46,228 &nbsp;&mdash;&nbsp; __________________________________________________<br/>"
                                              "(iii) 9,84,32,701 &nbsp;&mdash;&nbsp; __________________________________________________<br/>"
                                              "(iv) 74,52,283 &nbsp;&mdash;&nbsp; __________________________________________________<br/>"
                                              "(v) 4,80,498 &nbsp;&mdash;&nbsp; __________________________________________________",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 5] निम्न संख्याओं के परवर्ती (Successor) लिखिए",
                "questions": [
                    {"number": "9.", "text": "(i) 24,40,701 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) 1,00,199 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iii) 23,45,670<br/>"
                                              "(iv) 1,00,999 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (v) 9,999",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 6] निम्न संख्याओं के पूर्ववर्ती (Predecessor) लिखिए",
                "questions": [
                    {"number": "10.", "text": "(i) 94 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) 1,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iii) 2,08,090<br/>"
                                               "(iv) 7,654 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (v) 3,211",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 7] गुणनखंड (Factors) ज्ञात कीजिए",
                "questions": [
                    {"number": "11.", "text": "निम्न संख्याओं के सभी संभावित गुणनखंड लिखिए:<br/>"
                                               "(i) 24 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) 15 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iii) 27<br/>"
                                               "(iv) 18 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (v) 36",
                     "marks": "10", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


def get_paper_class7_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """त्रैमासिक परीक्षा सत्र - 2026-27
विषय - गणित
कक्षा - 7वीं
पूर्णांक: 50 | समय: 2.5 घंटे

प्रश्न 1] खाली स्थान भरिए: (5 अंक)
1] -53 + _________ = -53
2] [13 + (-12)] + (-7) = 13 + [(-12) + _________]
3] 369 ÷ _________ = 369
4] 20 ÷ _________ = -2
5] -75 ÷ _________ = -1

प्रश्न 2] निम्नलिखित गुणनफलों को ज्ञात कीजिए: (5 अंक)
1] (-15) x 0 x (-18)
2] (-12) x (-11) x 10
3] 3 x (-1)
4] (-316) x (-1)
5] (-3) x (-4) x (7)

प्रश्न 3] निम्न को सत्यापित कीजिए: (4 अंक)
18 x [7 + (-3)] = [18 x 7] + [18 x (-3)]

प्रश्न 4] a, b और c के निम्न मानों में से प्रत्येक के लिए a ÷ (b + c) ≠ (a ÷ b) + (a ÷ c) को सत्यापित कीजिए: (6 अंक)
(i) a = 12, b = -4, c = 2
(ii) a = (-10), b = 1, c = 1

प्रश्न 5] ज्ञात कीजिए: (4 अंक)
(i) 24 का 1/2
(ii) 18 का 2/3
(iii) 36 का 3/4
(iv) 35 का 4/5

प्रश्न 6] एक आयत का क्षेत्रफल ज्ञात कीजिए जिसकी लंबाई 5.7 सेमी और चौड़ाई 3 सेमी है। (4 अंक)

प्रश्न 7] ज्ञात कीजिए: (4 अंक)
(i) 1/4 का 1/4
(ii) 3/10 का 1/7
(iii) 2/9 का 1/7
(iv) 3/5 का 1/4

प्रश्न 8] निम्नलिखित भिन्नों का गुणा कीजिए: (8 अंक)
(i) 2/5 x 5 1/4
(ii) 6 2/5 x 7/9
(iii) 3 2/5 x 4/7
(iv) 2 3/5 x 3

प्रश्न 9] प्रथम 5 पूर्ण संख्याओं का माध्य ज्ञात कीजिए। (5 अंक)

प्रश्न 10] अपनी कक्षा के किन्हीं दस (10) विद्यार्थियों की ऊँचाइयों का परिसर ज्ञात कीजिए। (5 अंक)
"""
    structured = {
        "metadata": {
            "class_name": "Class_7",
            "subject": "Mathematics",
            "exam_type": "Quarterly",
            "time_allowed": "2.5 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "सभी प्रश्न अनिवार्य हैं।",
            "प्रत्येक प्रश्न के सम्मुख उनके अंक दिए गए हैं।"
        ],
        "sections": [
            {
                "title": "प्रश्न 1] रिक्त स्थानों की पूर्ति कीजिए",
                "questions": [
                    {"number": "1.", "text": "-53 + __________________ = -53", "marks": "1", "is_or_choice": False},
                    {"number": "2.", "text": "[13 + (-12)] + (-7) = 13 + [(-12) + __________________]", "marks": "1", "is_or_choice": False},
                    {"number": "3.", "text": "369 &divide; __________________ = 369", "marks": "1", "is_or_choice": False},
                    {"number": "4.", "text": "20 &divide; __________________ = -2", "marks": "1", "is_or_choice": False},
                    {"number": "5.", "text": "-75 &divide; __________________ = -1", "marks": "1", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 2] पूर्णांकों का गुणनफल ज्ञात कीजिए",
                "questions": [
                    {"number": "6.", "text": "(i) (-15) &times; 0 &times; (-18)<br/>"
                                              "(ii) (-12) &times; (-11) &times; 10<br/>"
                                              "(iii) 3 &times; (-1)<br/>"
                                              "(iv) (-316) &times; (-1)<br/>"
                                              "(v) (-3) &times; (-4) &times; (7)",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 3 एवं 4] वितरण एवं विभाजन गुणधर्म का सत्यापन",
                "questions": [
                    {"number": "7.", "text": "वितरण गुण का उपयोग करते हुए निम्न को सत्यापित कीजिए:<br/><b>18 &times; [7 + (-3)] = [18 &times; 7] + [18 &times; (-3)]</b>", "marks": "4", "is_or_choice": False},
                    {"number": "8.", "text": "a, b और c के निम्न मानों के लिए <b>a &divide; (b + c) &ne; (a &divide; b) + (a &divide; c)</b> को सत्यापित कीजिए:<br/>"
                                              "(i) a = 12, &nbsp; b = -4, &nbsp; c = 2<br/>"
                                              "(ii) a = (-10), &nbsp; b = 1, &nbsp; c = 1",
                     "marks": "6", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 5, 6 एवं 7] भिन्न एवं दशमलव के अनुप्रयोग",
                "questions": [
                    {"number": "9.", "text": "मान ज्ञात कीजिए:<br/>"
                                              "(i) 24 का 1/2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) 18 का 2/3<br/>"
                                              "(iii) 36 का 3/4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iv) 35 का 4/5",
                     "marks": "4", "is_or_choice": False},
                    {"number": "10.", "text": "एक आयत का क्षेत्रफल ज्ञात कीजिए जिसकी लंबाई 5.7 सेमी तथा चौड़ाई 3 सेमी है।", "marks": "4", "is_or_choice": False},
                    {"number": "11.", "text": "गुणनफल ज्ञात कीजिए:<br/>"
                                               "(i) 1/4 का 1/4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) 3/10 का 1/7<br/>"
                                               "(iii) 2/9 का 1/7 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iv) 3/5 का 1/4",
                     "marks": "4", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 8, 9 एवं 10] भिन्नों का गुणा व सांख्यिकी",
                "questions": [
                    {"number": "12.", "text": "निम्नलिखित भिन्नों का गुणा कीजिए एवं सरलतम रूप में लिखिए:<br/>"
                                               "(i) 2/5 &times; 5 1/4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) 6 2/5 &times; 7/9<br/>"
                                               "(iii) 3 2/5 &times; 4/7 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iv) 2 3/5 &times; 3",
                     "marks": "8", "is_or_choice": False},
                    {"number": "13.", "text": "प्रथम 5 पूर्ण संख्याओं (Whole numbers) का समांतर माध्य (Mean) ज्ञात कीजिए।", "marks": "5", "is_or_choice": False},
                    {"number": "14.", "text": "अपनी कक्षा के किन्हीं 10 विद्यार्थियों की अनुमानित ऊँचाइयों का परिसर (Range) ज्ञात कीजिए। (परिसर = अधिकतम मान - न्यूनतम मान)", "marks": "5", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


def get_paper_class8_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """त्रैमासिक परीक्षा 2026-27
विषय - गणित
कक्षा - 8वीं
पूर्णांक: 50 | समय: 2.5 घंटे

प्रश्न 1] खाली स्थान भरिए: (5 अंक)
1] त्रिभुज के तीनों कोणों का योग _________ होता है।
2] केवल रेखाखण्डों से घिरा बन्द वक्र _________ कहलाता है।
3] एक समांतर चतुर्भुज जिसके सभी कोण समकोण होते हैं _________ कहलाता है।
4] 4 का वर्ग _________ है।
5] -1/5 का व्युत्क्रम _________ होगा।

प्रश्न 2] निम्न समीकरणों को हल कीजिए तथा उत्तर की जांच कीजिए: (8 अंक)
1] 3x = 2x + 18
2] 5t - 3 = 3t - 5
3] 8x + 4 = 3(x - 1) + 7
4] x = 4/5 (x + 10)

प्रश्न 3] रैखिक समीकरणों को हल कीजिए: (8 अंक)
1] (x - 5)/3 = (x - 3)/5
2] x/2 - 1/5 = x/3 + 1/4
3] n/2 - 3n/4 + 5n/6 = 21
4] (3t - 2)/4 - (2t + 3)/3 = 2/3 - t

प्रश्न 4] निम्न समीकरणों को सरल रूप में बदलिए: (6 अंक)
1] 3(t - 3) = 5(2t + 1)
2] 0.25(4f - 3) = 0.05(10f - 9)

प्रश्न 5] एक सम बहुभुज के प्रत्येक बाह्य कोण का माप ज्ञात कीजिए: (6 अंक)
1] 9 भुजाएं
2] 15 भुजाएं
3] 8 भुजाएं
4] 6 भुजाएं

प्रश्न 6] निम्न आकृतियों में x का मान ज्ञात कीजिए: (6 अंक)
1] त्रिभुज के बाह्य कोण: 125°, 125°, x
2] पंचभुज के बाह्य कोण: 90°, 60°, 70°, x, 90°

प्रश्न 7] निम्न समांतर चतुर्भुजों में x, y, z के मान ज्ञात करो: (5 अंक)
1] समांतर चतुर्भुज ABCD जिसमें ∠B = 100°, ∠C = x, ∠D = y, ∠A = z
2] समांतर चतुर्भुज जिसमें एक कोण 80° है, बाह्य कोण z तथा अंतः कोण x, y हैं

प्रश्न 8] निम्न संख्याओं के वर्ग ज्ञात कीजिए: (6 अंक)
1] 32
2] 46
3] 86
"""
    structured = {
        "metadata": {
            "class_name": "Class_8",
            "subject": "Mathematics",
            "exam_type": "Quarterly",
            "time_allowed": "2.5 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "सभी प्रश्न अनिवार्य हैं।",
            "समीकरणों के हल में प्रत्येक चरण स्पष्ट प्रदर्शित कीजिए।"
        ],
        "sections": [
            {
                "title": "प्रश्न 1] रिक्त स्थानों की पूर्ति कीजिए",
                "questions": [
                    {"number": "1.", "text": "त्रिभुज के तीनों अंतःकोणों का योग __________________ होता है।", "marks": "1", "is_or_choice": False},
                    {"number": "2.", "text": "केवल रेखाखण्डों से बना सरल बन्द वक्र __________________ कहलाता है।", "marks": "1", "is_or_choice": False},
                    {"number": "3.", "text": "एक समांतर चतुर्भुज जिसके सभी कोण समकोण होते हैं __________________ कहलाता है।", "marks": "1", "is_or_choice": False},
                    {"number": "4.", "text": "4 का वर्ग __________________ है।", "marks": "1", "is_or_choice": False},
                    {"number": "5.", "text": "-1/5 का गुणात्मक प्रतिलोम (व्युत्क्रम) __________________ होगा।", "marks": "1", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 2] रैखिक समीकरणों को हल कर उत्तर की जांच कीजिए",
                "questions": [
                    {"number": "6.", "text": "3x = 2x + 18", "marks": "2", "is_or_choice": False},
                    {"number": "7.", "text": "5t - 3 = 3t - 5", "marks": "2", "is_or_choice": False},
                    {"number": "8.", "text": "8x + 4 = 3(x - 1) + 7", "marks": "2", "is_or_choice": False},
                    {"number": "9.", "text": "x = 4/5 (x + 10)", "marks": "2", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 3] रैखिक समीकरणों को हल कीजिए",
                "questions": [
                    {"number": "10.", "text": "(x - 5) / 3 = (x - 3) / 5", "marks": "2", "is_or_choice": False},
                    {"number": "11.", "text": "x / 2 - 1 / 5 = x / 3 + 1 / 4", "marks": "2", "is_or_choice": False},
                    {"number": "12.", "text": "n / 2 - 3n / 4 + 5n / 6 = 21", "marks": "2", "is_or_choice": False},
                    {"number": "13.", "text": "(3t - 2) / 4 - (2t + 3) / 3 = 2 / 3 - t", "marks": "2", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 4] समीकरणों को सरल रूप में बदलते हुए हल कीजिए",
                "questions": [
                    {"number": "14.", "text": "3(t - 3) = 5(2t + 1)", "marks": "3", "is_or_choice": False},
                    {"number": "15.", "text": "0.25(4f - 3) = 0.05(10f - 9)", "marks": "3", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 5] सम बहुभुज के बाह्य कोण की माप",
                "questions": [
                    {"number": "16.", "text": "एक सम बहुभुज के प्रत्येक बाह्य कोण का माप ज्ञात कीजिए जिसकी भुजाओं की संख्या हो:<br/>"
                                               "(i) 9 भुजाएँ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) 15 भुजाएँ<br/>"
                                               "(iii) 8 भुजाएँ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iv) 6 भुजाएँ",
                     "marks": "6", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 6 एवं 7] ज्यामितीय आकृतियों में अज्ञात कोण",
                "questions": [
                    {"number": "17.", "text": "निम्न ज्यामितीय आकृतियों में अज्ञात कोण x का मान ज्ञात कीजिए:<br/>"
                                               "(i) एक त्रिभुज जिसके दो बाह्य कोण क्रमशः 125&deg; तथा 125&deg; हैं, तीसरे बाह्य कोण x का मान ज्ञात कीजिए।<br/>"
                                               "(ii) एक पंचभुज जिसके बाह्य कोण क्रमशः 90&deg;, 60&deg;, 70&deg;, x एवं 90&deg; हैं, x का मान ज्ञात कीजिए।",
                     "marks": "6", "is_or_choice": False},
                    {"number": "18.", "text": "निम्न समांतर चतुर्भुजों में अज्ञात कोणों x, y, z के मान ज्ञात कीजिए:<br/>"
                                               "(i) समांतर चतुर्भुज ABCD में यदि &ang;B = 100&deg; हो, तो &ang;C = x, &ang;D = y, &ang;A = z का मान ज्ञात कीजिए।<br/>"
                                               "(ii) एक समांतर चतुर्भुज में संलग्न कोण 80&deg; दिया गया है, तो बाह्य कोण z तथा अंतः कोणों x और y का मान ज्ञात कीजिए।",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "प्रश्न 8] वर्ग ज्ञात कीजिए",
                "questions": [
                    {"number": "19.", "text": "निम्नलिखित संख्याओं के वर्ग ज्ञात कीजिए:<br/>"
                                               "(i) 32 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) 46 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iii) 86",
                     "marks": "6", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured
