"""
High-fidelity verified handwritten exam paper transcripts and structured sections
for Swami Pradeep Public School - English Series.

Covers:
- Class KG 1 & 2 English (english 1.pdf)
- Class 1 English (english 2.pdf)
- Class 2 English (english 3.pdf)
- Class 3 English (english 4.pdf)
- Class 4 English (english 5.pdf)
- Class 5 English (english 6.pdf)
- Class 6 English (english 8.pdf)
- Class 8 English (english 9.pdf)
"""

from typing import Tuple, Dict, Any

# ==============================================================================
# 1. ENGLISH CLASS KG1 & KG2 (english 1.pdf)
# ==============================================================================
def get_paper_english_kg_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """Swami Pradeep Public School
Quarterly Examination - 2026-27
Subject - English
Class - K.g.I + K.g.II
Max Marks: 50 | Time: 2.0 Hours

Question-1] Match the following (Capital letters with Small letters) (10 Marks):
A - b
B - a
C - d
D - c
E - f
F - e
G - h
H - g

Question-2] Fill in the blanks (Alphabet Sequence) (10 Marks):
A ___ C ___ E ___ ___ H ___ J ___
L ___ ___ O ___ Q ___ S ___ ___

Question 3] Write the Capital letters (A to Z) (10 Marks):
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

Question 4] Write the small letters (a to z) (10 Marks):
a b c d e f g h i j k l m n o p q r s t u v w x y z

Question 5] Write four fruits name (Fill the missing letters) (10 Marks):
1. A _ _ l _ (Apple)
2. B _ n _ _ a (Banana)
3. O _ a _ g _ (Orange)
4. P _ _ _ y _ (Papaya)
"""
    structured = {
        "metadata": {
            "class_name": "Class_KG",
            "subject": "English",
            "exam_type": "Quarterly",
            "time_allowed": "2.0 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "All questions are compulsory.",
            "Write neatly in the lines provided."
        ],
        "sections": [
            {
                "title": "Question 1: Match Capital with Small Letters",
                "questions": [
                    {"number": "1.", "text": "Match the <b>Capital Letters</b> with their corresponding <b>Small Letters</b>:<br/><br/>"
                                              "<table style='width: 60%; border-collapse: collapse; margin-left: 20px;'>"
                                              "<tr><th style='text-align: left;'><b>Capital</b></th><th style='text-align: left;'><b>Small</b></th></tr>"
                                              "<tr><td><b>A</b></td><td>— &nbsp; b</td></tr>"
                                              "<tr><td><b>B</b></td><td>— &nbsp; a</td></tr>"
                                              "<tr><td><b>C</b></td><td>— &nbsp; d</td></tr>"
                                              "<tr><td><b>D</b></td><td>— &nbsp; c</td></tr>"
                                              "<tr><td><b>E</b></td><td>— &nbsp; f</td></tr>"
                                              "<tr><td><b>F</b></td><td>— &nbsp; e</td></tr>"
                                              "<tr><td><b>G</b></td><td>— &nbsp; h</td></tr>"
                                              "<tr><td><b>H</b></td><td>— &nbsp; g</td></tr>"
                                              "</table>",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 2: Missing Letters in Alphabet",
                "questions": [
                    {"number": "2.", "text": "Fill in the blanks to complete the letter sequence:<br/><br/>"
                                              "<b>A</b> &nbsp; ______ &nbsp; <b>C</b> &nbsp; ______ &nbsp; <b>E</b> &nbsp; ______ &nbsp; ______ &nbsp; <b>H</b> &nbsp; ______ &nbsp; <b>J</b> &nbsp; ______<br/><br/>"
                                              "<b>L</b> &nbsp; ______ &nbsp; ______ &nbsp; <b>O</b> &nbsp; ______ &nbsp; <b>Q</b> &nbsp; ______ &nbsp; <b>S</b> &nbsp; ______ &nbsp; ______",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 3 & 4: Capital & Small Alphabet Writing",
                "questions": [
                    {"number": "3.", "text": "Write the <b>Capital Letters (A to Z)</b> neatly in the box below:<br/><br/>"
                                              "<div style='border: 1px dashed #666; height: 95px; width: 100%; border-radius: 4px;'></div>",
                     "marks": "10", "is_or_choice": False},
                    {"number": "4.", "text": "Write the <b>Small Letters (a to z)</b> neatly in the box below:<br/><br/>"
                                              "<div style='border: 1px dashed #666; height: 95px; width: 100%; border-radius: 4px;'></div>",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 5: Fruits Name Spelling",
                "questions": [
                    {"number": "5.", "text": "Fill in the missing letters to complete the names of fruits:<br/><br/>"
                                              "1. <b>A &nbsp; [ &nbsp;&nbsp; ] &nbsp; [ &nbsp;&nbsp; ] &nbsp; L &nbsp; [ &nbsp;&nbsp; ]</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                                              "2. <b>B &nbsp; [ &nbsp;&nbsp; ] &nbsp; N &nbsp; [ &nbsp;&nbsp; ] &nbsp; N &nbsp; [ &nbsp;&nbsp; ]</b><br/><br/>"
                                              "3. <b>O &nbsp; [ &nbsp;&nbsp; ] &nbsp; A &nbsp; [ &nbsp;&nbsp; ] &nbsp; G &nbsp; [ &nbsp;&nbsp; ]</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                                              "4. <b>P &nbsp; [ &nbsp;&nbsp; ] &nbsp; P &nbsp; [ &nbsp;&nbsp; ] &nbsp; Y &nbsp; [ &nbsp;&nbsp; ]</b>",
                     "marks": "10", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


# ==============================================================================
# 2. ENGLISH CLASS 1 (english 2.pdf)
# ==============================================================================
def get_paper_english_class1_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """Swami Pradeep Public School
Quarterly Examination 2026-2027
Class 1st
Subject - English
Max Marks: 50 | Time: 2.0 Hours

Que 1. Meanings (Write Hindi meanings) (10 Marks):
Cow - ______
dog - ______
king - ______
queen - ______
Sun - ______
blue - ______
red - ______
pink - ______
apple - ______
Mango - ______

Que 2. Complete these words with 'e' (5 Marks):
1. k_y
2. orang_
3. appl_
4. hors_
5. blu_

Que 3. Write the alphabet (A to Z) (10 Marks)

Que 4. Match the numbers with the number words (10 Marks):
1 - five
2 - four
3 - one
4 - two
5 - three
6 - eight
7 - nine
8 - ten
9 - six
10 - seven

Que 5. What is your name? (5 Marks)
Ans: My name is ____________________________________

Que 6. Write the fruits name (any 5) (5 Marks):
1. ______ 2. ______ 3. ______ 4. ______ 5. ______

Que 7. Write the vegetables names (any 5) (5 Marks):
1. ______ 2. ______ 3. ______ 4. ______ 5. ______
"""
    structured = {
        "metadata": {
            "class_name": "Class_1",
            "subject": "English",
            "exam_type": "Quarterly",
            "time_allowed": "2.0 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "All questions are compulsory.",
            "Write answers neatly and clearly."
        ],
        "sections": [
            {
                "title": "Question 1: Word Meanings",
                "questions": [
                    {"number": "1.", "text": "Write the Hindi meaning of the following English words:<br/>"
                                              "(i) <b>Cow</b> &nbsp;&mdash;&nbsp; ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) <b>Dog</b> &nbsp;&mdash;&nbsp; ________________________<br/>"
                                              "(iii) <b>King</b> &nbsp;&mdash;&nbsp; ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iv) <b>Queen</b> &nbsp;&mdash;&nbsp; ________________________<br/>"
                                              "(v) <b>Sun</b> &nbsp;&mdash;&nbsp; ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (vi) <b>Blue</b> &nbsp;&mdash;&nbsp; ________________________<br/>"
                                              "(vii) <b>Red</b> &nbsp;&mdash;&nbsp; ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (viii) <b>Pink</b> &nbsp;&mdash;&nbsp; ________________________<br/>"
                                              "(ix) <b>Apple</b> &nbsp;&mdash;&nbsp; ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (x) <b>Mango</b> &nbsp;&mdash;&nbsp; ________________________",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 2 & 3: Word Completion & Alphabet",
                "questions": [
                    {"number": "2.", "text": "Complete each word by filling the missing letter <b>'e'</b>:<br/>"
                                              "1. <b>k __ y</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. <b>orang __</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. <b>appl __</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4. <b>hors __</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5. <b>blu __</b>",
                     "marks": "5", "is_or_choice": False},
                    {"number": "3.", "text": "Write all 26 English alphabets <b>(A to Z)</b> in proper order:<br/><br/>"
                                              "<div style='border: 1px dashed #666; height: 90px; width: 100%; border-radius: 4px;'></div>",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 4: Match Numbers with Number Words",
                "questions": [
                    {"number": "4.", "text": "Match the numerals with their correct number names:<br/><br/>"
                                              "<table style='width: 70%; border-collapse: collapse; margin-left: 20px;'>"
                                              "<tr><th style='text-align: left;'><b>Number</b></th><th style='text-align: left;'><b>Word</b></th><th style='text-align: left;'><b>Number</b></th><th style='text-align: left;'><b>Word</b></th></tr>"
                                              "<tr><td>1</td><td>— &nbsp; five</td><td>6</td><td>— &nbsp; eight</td></tr>"
                                              "<tr><td>2</td><td>— &nbsp; four</td><td>7</td><td>— &nbsp; nine</td></tr>"
                                              "<tr><td>3</td><td>— &nbsp; one</td><td>8</td><td>— &nbsp; ten</td></tr>"
                                              "<tr><td>4</td><td>— &nbsp; two</td><td>9</td><td>— &nbsp; six</td></tr>"
                                              "<tr><td>5</td><td>— &nbsp; three</td><td>10</td><td>— &nbsp; seven</td></tr>"
                                              "</table>",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 5, 6 & 7: Vocabulary & General Identity",
                "questions": [
                    {"number": "5.", "text": "<b>What is your name?</b><br/>"
                                              "Ans: My name is ____________________________________________________________________.",
                     "marks": "5", "is_or_choice": False},
                    {"number": "6.", "text": "Write the names of any <b>five fruits</b>:<br/>"
                                              "1. ______________ &nbsp;&nbsp; 2. ______________ &nbsp;&nbsp; 3. ______________ &nbsp;&nbsp; 4. ______________ &nbsp;&nbsp; 5. ______________",
                     "marks": "5", "is_or_choice": False},
                    {"number": "7.", "text": "Write the names of any <b>five vegetables</b>:<br/>"
                                              "1. ______________ &nbsp;&nbsp; 2. ______________ &nbsp;&nbsp; 3. ______________ &nbsp;&nbsp; 4. ______________ &nbsp;&nbsp; 5. ______________",
                     "marks": "5", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


# ==============================================================================
# 3. ENGLISH CLASS 2 (english 3.pdf)
# ==============================================================================
def get_paper_english_class2_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """Swami Pradeep Public School
Quarterly Examination 2026-2027
Class 2nd
Subject - English
Max Marks: 50 | Time: 2.0 Hours

Que 1. Meaning (Write Hindi meanings) (10 Marks):
girl, boy, sister, king, cow, lion, horse, queen, son, water

Que 2. Match the words with their opposites (5 Marks):
p.m. - stand
sit - after
before - go
come - old
new - a.m.

Que 3. Write each as one word (Compound words) (5 Marks):
(i) any + one = ______
(ii) any + thing = ______
(iii) any + where = ______
(iv) no + thing = ______
(v) no + body = ______

Que 4. Complete these words with 'o' (5 Marks):
(i) T_p
(ii) b_x
(iii) pian_
(iv) b_dy
(v) fr_ck

Que 5. Complete each sentence with the right word [Cave, hole, nest, kennel, water] (5 Marks):
1. A fish lives in ______
2. A dog lives in a ______
3. A bird lives in a ______
4. A lion lives in a ______
5. A mouse lives in a ______

Que 6. Write the fruits name (any 5) (5 Marks)
Que 7. Write the vegetables name (any 5) (5 Marks)
Que 8. Write the body parts name (any 6) (5 Marks)
Que 9. Write the vowels (5 Marks)
"""
    structured = {
        "metadata": {
            "class_name": "Class_2",
            "subject": "English",
            "exam_type": "Quarterly",
            "time_allowed": "2.0 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "All questions are compulsory.",
            "Write answers in a clear and neat handwriting."
        ],
        "sections": [
            {
                "title": "Question 1: Word Meanings",
                "questions": [
                    {"number": "1.", "text": "Write the Hindi meanings of the given English words:<br/>"
                                              "(i) <b>girl</b> &nbsp;&mdash;&nbsp; ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) <b>boy</b> &nbsp;&mdash;&nbsp; ________________________<br/>"
                                              "(iii) <b>sister</b> &nbsp;&mdash;&nbsp; ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iv) <b>king</b> &nbsp;&mdash;&nbsp; ________________________<br/>"
                                              "(v) <b>cow</b> &nbsp;&mdash;&nbsp; ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (vi) <b>lion</b> &nbsp;&mdash;&nbsp; ________________________<br/>"
                                              "(vii) <b>horse</b> &nbsp;&mdash;&nbsp; ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (viii) <b>queen</b> &nbsp;&mdash;&nbsp; ________________________<br/>"
                                              "(ix) <b>son</b> &nbsp;&mdash;&nbsp; ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (x) <b>water</b> &nbsp;&mdash;&nbsp; ________________________",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 2 & 3: Opposites & Compound Words",
                "questions": [
                    {"number": "2.", "text": "Match the words with their correct <b>opposites</b>:<br/><br/>"
                                              "<table style='width: 60%; border-collapse: collapse; margin-left: 20px;'>"
                                              "<tr><th style='text-align: left;'><b>Word</b></th><th style='text-align: left;'><b>Opposite</b></th></tr>"
                                              "<tr><td>p.m.</td><td>— &nbsp; stand</td></tr>"
                                              "<tr><td>sit</td><td>— &nbsp; after</td></tr>"
                                              "<tr><td>before</td><td>— &nbsp; go</td></tr>"
                                              "<tr><td>come</td><td>— &nbsp; old</td></tr>"
                                              "<tr><td>new</td><td>— &nbsp; a.m.</td></tr>"
                                              "</table>",
                     "marks": "5", "is_or_choice": False},
                    {"number": "3.", "text": "Combine and write each pair as <b>one word</b>:<br/>"
                                              "(i) any + one &nbsp;=&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                                              "(ii) any + thing &nbsp;=&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b><br/>"
                                              "(iii) any + where &nbsp;=&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                                              "(iv) no + thing &nbsp;=&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b><br/>"
                                              "(v) no + body &nbsp;=&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b>",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 4 & 5: Word Completion & Animal Homes",
                "questions": [
                    {"number": "4.", "text": "Complete the words with the vowel <b>'o'</b>:<br/>"
                                              "(i) <b>T __ p</b> &nbsp;&nbsp;&nbsp;&nbsp; (ii) <b>b __ x</b> &nbsp;&nbsp;&nbsp;&nbsp; (iii) <b>pian __</b> &nbsp;&nbsp;&nbsp;&nbsp; (iv) <b>b __ dy</b> &nbsp;&nbsp;&nbsp;&nbsp; (v) <b>fr __ ck</b>",
                     "marks": "5", "is_or_choice": False},
                    {"number": "5.", "text": "Fill each blank with the correct home: <b>[ Cave, hole, nest, kennel, water ]</b><br/>"
                                              "1. A fish lives in __________________.<br/>"
                                              "2. A dog lives in a __________________.<br/>"
                                              "3. A bird lives in a __________________.<br/>"
                                              "4. A lion lives in a __________________.<br/>"
                                              "5. A mouse lives in a __________________.",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 6, 7, 8 & 9: Vocabulary, Body Parts & Vowels",
                "questions": [
                    {"number": "6.", "text": "Write the names of any <b>five fruits</b>: 1. ______ 2. ______ 3. ______ 4. ______ 5. ______", "marks": "5", "is_or_choice": False},
                    {"number": "7.", "text": "Write the names of any <b>five vegetables</b>: 1. ______ 2. ______ 3. ______ 4. ______ 5. ______", "marks": "5", "is_or_choice": False},
                    {"number": "8.", "text": "Write the names of any <b>six parts of the body</b>: 1. ______ 2. ______ 3. ______ 4. ______ 5. ______ 6. ______", "marks": "5", "is_or_choice": False},
                    {"number": "9.", "text": "Write the <b>five vowels</b> of English alphabet: 1. ______ 2. ______ 3. ______ 4. ______ 5. ______", "marks": "5", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


# ==============================================================================
# 4. ENGLISH CLASS 3 (english 4.pdf)
# ==============================================================================
def get_paper_english_class3_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """Swami Pradeep Public School
Quarterly Examination 2026-2027
Class 3rd
Subject - English
Max Marks: 50 | Time: 2.5 Hours

Que 1. Meaning (Any 10) (10 Marks):
Wagging, Belly, Stretched, Sitting, Swing, Up, Task, Straighten, Sweat, Weeds, Disappeared, God.

Que 2. Match the following to make sentences (5 Marks):
A dog - Cries
A baby - dries
A towel - teaches
A teacher - kicks
A Footballer - yelps

Que 3. Put the sentences in their right order (Story of King Midas) (5 Marks):
[ ] Everything Midas touched turned into gold.
[ ] Midas was sad when his daughter turned into gold.
[ ] Dionysus gave Midas the gift of the golden touch.
[ ] Dionysus advised Midas to go and bathe in the pactolus river.
[ ] Midas requested the god to take back his gift of the golden touch.

Que 4. Write opposites of the following words (5 Marks):
1. hot
2. open
3. fast
4. up
5. day

Que 5. Answer the following questions (Any 5) (10 Marks):
1. What was Mr. Roy doing in his room?
2. What did the boy take out of his bag?
3. How did the genie look?
4. What did the genie build for the farmer?
5. Who was Dionysus?
6. Where were the rabbits going?
7. Where was the man going?

Que 6. Write the application leave for two days (7 Marks)

Que 7. Write an essay on the given topics (8 Marks):
[1] The Cow  /  [2] My School
"""
    structured = {
        "metadata": {
            "class_name": "Class_3",
            "subject": "English",
            "exam_type": "Quarterly",
            "time_allowed": "2.5 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "All questions are compulsory unless internal choice is specified.",
            "Write answers neatly and clearly."
        ],
        "sections": [
            {
                "title": "Question 1: Word Meanings (Any 10)",
                "questions": [
                    {"number": "1.", "text": "Write the Hindi meaning of <b>any ten</b> of the following words:<br/>"
                                              "<b>Wagging, Belly, Stretched, Sitting, Swing, Up, Task, Straighten, Sweat, Weeds, Disappeared, God.</b>",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 2: Sentence Matching",
                "questions": [
                    {"number": "2.", "text": "Match the columns to make meaningful sentences:<br/><br/>"
                                              "<table style='width: 65%; border-collapse: collapse; margin-left: 20px;'>"
                                              "<tr><th style='text-align: left;'><b>Subject</b></th><th style='text-align: left;'><b>Action</b></th></tr>"
                                              "<tr><td>A dog</td><td>— &nbsp; Cries</td></tr>"
                                              "<tr><td>A baby</td><td>— &nbsp; dries</td></tr>"
                                              "<tr><td>A towel</td><td>— &nbsp; teaches</td></tr>"
                                              "<tr><td>A teacher</td><td>— &nbsp; kicks</td></tr>"
                                              "<tr><td>A Footballer</td><td>— &nbsp; yelps</td></tr>"
                                              "</table>",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 3: Story Sequencing",
                "questions": [
                    {"number": "3.", "text": "Number the sentences in their <b>correct sequential order (1 to 5)</b>:<br/>"
                                              "[ &nbsp;&nbsp; ] Everything Midas touched turned into gold.<br/>"
                                              "[ &nbsp;&nbsp; ] Midas was sad when his daughter turned into gold.<br/>"
                                              "[ &nbsp;&nbsp; ] Dionysus gave Midas the gift of the golden touch.<br/>"
                                              "[ &nbsp;&nbsp; ] Dionysus advised Midas to go and bathe in the Pactolus river.<br/>"
                                              "[ &nbsp;&nbsp; ] Midas requested the god to take back his gift of the golden touch.",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 4: Antonyms (Opposites)",
                "questions": [
                    {"number": "4.", "text": "Write the opposites of the following words:<br/>"
                                              "1. hot &times; ______________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. open &times; ______________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. fast &times; ______________<br/>"
                                              "4. up &times; ______________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5. day &times; ______________",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 5: Comprehension Questions (Any 5)",
                "questions": [
                    {"number": "5.", "text": "Answer <b>any five</b> of the following questions:<br/>"
                                              "1. What was Mr. Roy doing in his room?<br/>"
                                              "2. What did the boy take out of his bag?<br/>"
                                              "3. How did the genie look?<br/>"
                                              "4. What did the genie build for the farmer?<br/>"
                                              "5. Who was Dionysus?<br/>"
                                              "6. Where were the rabbits going?<br/>"
                                              "7. Where was the man going?",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 6: Application Writing",
                "questions": [
                    {"number": "6.", "text": "Write an application to your Headmaster/Principal requesting <b>leave for two days</b> due to urgent work or illness.",
                     "marks": "7", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 7: Essay Writing",
                "questions": [
                    {"number": "7.", "text": "Write an essay in about 8-10 lines on any one of the following topics:<br/>"
                                              "[1] <b>The Cow</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [2] <b>My School</b>",
                     "marks": "8", "is_or_choice": True}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


# ==============================================================================
# 5. ENGLISH CLASS 4 (english 5.pdf)
# ==============================================================================
def get_paper_english_class4_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """Swami Pradeep Public School
Quarterly Examination 2026-2027
Class 4th
Subject - English
Max Marks: 50 | Time: 2.5 Hours

Que 1. Meaning (Any 10) (10 Marks):
Say, Throw, Bow, Grown, Glad, Want, Cage, Put, Disappear, Roll, Still, Surprise.

Que 2. Complete the sentences using the given words [Sky, baby bird, market, wool ball, Orange] (5 Marks):
1. Appu went to ______
2. Appu wanted to buy some ______
3. The moon shines in the ______
4. The cat was running after a ______
5. Raju and Mona found a ______

Que 3. Write [T] for True and [F] for False Statements (5 Marks):
1. Ratty, the rat cut the cage open. [   ]
2. The cat was rolling down. [   ]
3. Raju, Shalu and Kalu like fun. [   ]
4. The stars do not shine at night. [   ]
5. The moon is always round like an 'O'. [   ]

Que 4. Rearrange the letters to make a word (5 Marks):
1. rgonud -> ______
2. yoj -> ______
3. ylf -> ______
4. elrth -> ______
5. usn -> ______

Que 5. Match the following (Short forms / Contractions) (5 Marks):
1. I will - I'll Call
2. I will call - It's Fun
3. I cannot - I haven't
4. I have not - I can't
5. It is fun - I'll

Que 6. Answer these questions (Any 5) (10 Marks):
1. Where was he going?
2. What was the name of the ant?
3. What is grandma doing?
4. What is rolling down?
5. Is the grandma far or near?
6. What happened to the ball?

Que 7. Write the application leave for two days (5 Marks)

Que 8. Write the essay given topics: [1] The Cow / [2] My School (5 Marks)
"""
    structured = {
        "metadata": {
            "class_name": "Class_4",
            "subject": "English",
            "exam_type": "Quarterly",
            "time_allowed": "2.5 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "All questions are compulsory.",
            "Write answers clearly and in proper grammatical sentences."
        ],
        "sections": [
            {
                "title": "Question 1: Word Meanings (Any 10)",
                "questions": [
                    {"number": "1.", "text": "Write the Hindi meaning of <b>any ten</b> of the following words:<br/>"
                                              "<b>Say, Throw, Bow, Grown, Glad, Want, Cage, Put, Disappear, Roll, Still, Surprise.</b>",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 2: Fill in the Blanks",
                "questions": [
                    {"number": "2.", "text": "Complete the sentences choosing appropriate words from the box:<br/>"
                                              "<b>[ Sky, baby bird, market, wool ball, Orange ]</b><br/>"
                                              "1. Appu went to the __________________.<br/>"
                                              "2. Appu wanted to buy some __________________.<br/>"
                                              "3. The moon shines in the __________________.<br/>"
                                              "4. The cat was running after a __________________.<br/>"
                                              "5. Raju and Mona found a __________________.",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 3: True or False Statements",
                "questions": [
                    {"number": "3.", "text": "Write <b>[T]</b> for True and <b>[F]</b> for False statements:<br/>"
                                              "1. Ratty, the rat cut the cage open. &nbsp;&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b><br/>"
                                              "2. The cat was rolling down. &nbsp;&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b><br/>"
                                              "3. Raju, Shalu and Kalu like fun. &nbsp;&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b><br/>"
                                              "4. The stars do not shine at night. &nbsp;&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b><br/>"
                                              "5. The moon is always round like an 'O'. &nbsp;&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b>",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 4: Word Scramble",
                "questions": [
                    {"number": "4.", "text": "Rearrange the jumbled letters to form meaningful words:<br/>"
                                              "1. <b>rgonud</b> &nbsp;&rarr;&nbsp; ____________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. <b>yoj</b> &nbsp;&rarr;&nbsp; ____________________<br/>"
                                              "3. <b>ylf</b> &nbsp;&rarr;&nbsp; ____________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4. <b>elrth (earth)</b> &nbsp;&rarr;&nbsp; ____________________<br/>"
                                              "5. <b>usn</b> &nbsp;&rarr;&nbsp; ____________________",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 5: Contractions / Short Forms",
                "questions": [
                    {"number": "5.", "text": "Match the full forms with their correct contracted short forms:<br/><br/>"
                                              "<table style='width: 65%; border-collapse: collapse; margin-left: 20px;'>"
                                              "<tr><th style='text-align: left;'><b>Full Form</b></th><th style='text-align: left;'><b>Short Form</b></th></tr>"
                                              "<tr><td>1. I will</td><td>— &nbsp; I'll Call</td></tr>"
                                              "<tr><td>2. I will call</td><td>— &nbsp; It's Fun</td></tr>"
                                              "<tr><td>3. I cannot</td><td>— &nbsp; I haven't</td></tr>"
                                              "<tr><td>4. I have not</td><td>— &nbsp; I can't</td></tr>"
                                              "<tr><td>5. It is fun</td><td>— &nbsp; I'll</td></tr>"
                                              "</table>",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 6: Textual Questions (Any 5)",
                "questions": [
                    {"number": "6.", "text": "Answer <b>any five</b> of the following questions:<br/>"
                                              "1. Where was he going?<br/>"
                                              "2. What was the name of the ant?<br/>"
                                              "3. What is grandma doing?<br/>"
                                              "4. What is rolling down the hill?<br/>"
                                              "5. Is the grandma far or near?<br/>"
                                              "6. What happened to the ball?",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 7 & 8: Writing Skills",
                "questions": [
                    {"number": "7.", "text": "Write an application to the Headmaster requesting <b>leave for two days</b>.", "marks": "5", "is_or_choice": False},
                    {"number": "8.", "text": "Write an essay on any one of the given topics:<br/>"
                                              "[1] <b>The Cow</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [2] <b>My School</b>",
                     "marks": "5", "is_or_choice": True}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


# ==============================================================================
# 6. ENGLISH CLASS 5 (english 6.pdf)
# ==============================================================================
def get_paper_english_class5_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """Swami Pradeep Public School
Quarterly Examination - 2026-27
Class - 5th
Subject - English
Max Marks: 50 | Time: 2.5 Hours

1. Circle the odd ones (5 Marks):
i. Flower, grass, bird, tree
ii. Bird, bee, butterfly, buffalo
iii. Song, food, clothe, home
iv. Father, brother, sister, singer
v. Book, pencil, water, pen

2. Fill in the blanks [Driver, teacher, the fifth, pilot, dog] (5 Marks):
i. A ______ lives in a kennel.
ii. One who teaches is a ______.
iii. Friday is ______ day of the week.
iv. One who flies an aeroplane is a ______.
v. One who drives a car is a ______.

3. Give opposites of the following words (10 Marks):
take x ______
out x ______
hot x ______
forward x ______
before x ______
high x ______
never x ______
girl x ______
aunt x ______
bitch x ______

4. Match the following (Word with meaning) (5 Marks):
Humid - to take away something forcefully
Chattering - very religious person
devotee - speed
snatch - warm and damp
Pace - sound made by monkeys

5. Answer these questions (any 5) (15 Marks):
1. Why should we be thankful to god?
2. What shines during the day?
3. Who was walking along the ghats?
4. Why do the people go to these places?
5. Where did the children go to learn through computers?
6. Into how many groups were the children divided?

6. Write an application for leave for three days (10 Marks)
"""
    structured = {
        "metadata": {
            "class_name": "Class_5",
            "subject": "English",
            "exam_type": "Quarterly",
            "time_allowed": "2.5 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "All questions are compulsory unless internal choice is specified.",
            "Write answers neatly and legibly."
        ],
        "sections": [
            {
                "title": "Section 1: Odd One Out",
                "questions": [
                    {"number": "1.", "text": "Identify and circle the <b>odd one</b> out in each group:<br/>"
                                              "(i) Flower &nbsp;&nbsp;&bull;&nbsp;&nbsp; grass &nbsp;&nbsp;&bull;&nbsp;&nbsp; <b>bird</b> &nbsp;&nbsp;&bull;&nbsp;&nbsp; tree<br/>"
                                              "(ii) Bird &nbsp;&nbsp;&bull;&nbsp;&nbsp; bee &nbsp;&nbsp;&bull;&nbsp;&nbsp; butterfly &nbsp;&nbsp;&bull;&nbsp;&nbsp; <b>buffalo</b><br/>"
                                              "(iii) <b>Song</b> &nbsp;&nbsp;&bull;&nbsp;&nbsp; food &nbsp;&nbsp;&bull;&nbsp;&nbsp; clothe &nbsp;&nbsp;&bull;&nbsp;&nbsp; home<br/>"
                                              "(iv) Father &nbsp;&nbsp;&bull;&nbsp;&nbsp; brother &nbsp;&nbsp;&bull;&nbsp;&nbsp; sister &nbsp;&nbsp;&bull;&nbsp;&nbsp; <b>singer</b><br/>"
                                              "(v) Book &nbsp;&nbsp;&bull;&nbsp;&nbsp; pencil &nbsp;&nbsp;&bull;&nbsp;&nbsp; <b>water</b> &nbsp;&nbsp;&bull;&nbsp;&nbsp; pen",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Section 2: Fill in the Blanks",
                "questions": [
                    {"number": "2.", "text": "Fill in the blanks with the correct words from the box:<br/>"
                                              "<b>[ Driver, teacher, the fifth, pilot, dog ]</b><br/>"
                                              "(i) A __________________ lives in a kennel.<br/>"
                                              "(ii) One who teaches in a school is a __________________.<br/>"
                                              "(iii) Friday is __________________ day of the week.<br/>"
                                              "(iv) One who flies an aeroplane is a __________________.<br/>"
                                              "(v) One who drives a motor car is a __________________.",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Section 3: Antonyms (Opposites)",
                "questions": [
                    {"number": "3.", "text": "Write the opposites of the following words:<br/>"
                                              "(i) take &times; ______________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) high &times; ______________<br/>"
                                              "(iii) out &times; ______________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iv) never &times; ______________<br/>"
                                              "(v) hot &times; ______________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (vi) girl &times; ______________<br/>"
                                              "(vii) forward &times; ____________ &nbsp;&nbsp;&nbsp;&nbsp; (viii) aunt &times; ______________<br/>"
                                              "(ix) before &times; ____________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (x) bitch &times; ______________",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Section 4: Vocabulary Matching",
                "questions": [
                    {"number": "4.", "text": "Match the words with their correct meanings:<br/><br/>"
                                              "<table style='width: 75%; border-collapse: collapse; margin-left: 20px;'>"
                                              "<tr><th style='text-align: left;'><b>Word</b></th><th style='text-align: left;'><b>Meaning</b></th></tr>"
                                              "<tr><td>Humid</td><td>— &nbsp; to take away something forcefully</td></tr>"
                                              "<tr><td>Chattering</td><td>— &nbsp; very religious person</td></tr>"
                                              "<tr><td>devotee</td><td>— &nbsp; speed</td></tr>"
                                              "<tr><td>snatch</td><td>— &nbsp; warm and damp</td></tr>"
                                              "<tr><td>Pace</td><td>— &nbsp; sound made by monkeys</td></tr>"
                                              "</table>",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Section 5: Comprehension Questions (Any 5)",
                "questions": [
                    {"number": "5.", "text": "Answer <b>any five</b> of the following questions:<br/>"
                                              "1. Why should we be thankful to God?<br/>"
                                              "2. What shines brightly during the day?<br/>"
                                              "3. Who was walking along the ghats of the river?<br/>"
                                              "4. Why do people visit these historical places?<br/>"
                                              "5. Where did the children go to learn through computers?<br/>"
                                              "6. Into how many groups were the children divided?",
                     "marks": "15", "is_or_choice": False}
                ]
            },
            {
                "title": "Section 6: Application Writing",
                "questions": [
                    {"number": "6.", "text": "Write an application to the Principal of your school requesting <b>leave for three days</b> due to urgent domestic work.",
                     "marks": "10", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


# ==============================================================================
# 7. ENGLISH CLASS 6 (english 8.pdf)
# ==============================================================================
def get_paper_english_class6_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """Swami Pradeep Public School
Quarterly Examination - 2026-27
Class - 6th
Subject - English
Max Marks: 50 | Time: 2.5 Hours

Q1. Meaning (Any 10) (10 Marks):
brave, country, insect, soldiers, favour, cattle, attack, prompt, impression, try, sparrows, village

Q2. Fill in the blanks choosing correct words [tree, prompt, soldiers, worried, branches] (5 Marks):
1. The teacher tried to ______ Gandhiji.
2. He was very sad and ______.
3. The tree spread its ______.
4. Many of his ______ were killed.
5. I like the mango ______.

Q3. Match column 'A' with column 'B' (5 Marks):
1. sad - a fifty years old banyan tree
2. The story is about - swing on its branches
3. The children - sit under it to take rest
4. The people - take rest and sleep in it
5. The birds - happy

Q4. Tick [✓] or [✗] (5 Marks):
1. The spider did not succeed in climbing. [ ]
2. It is a pleasant thing to sway in a swing. [ ]
3. It was a fifty years old mango tree. [ ]
4. Gandhiji misspelt the word kettle. [ ]
5. Gandhiji left Porbandar at the age of eight. [ ]

Q5. Answer these questions (any 5) (15 Marks):
1. Where do we get fresh air from?
2. What does the child see in the countryside?
3. Who attacked his country?
4. When was Mahatma Gandhi born?
5. What kind of ruler was the king?
6. What does the child see when he is up in the air?

Q7. Write the application leave for three days (10 Marks)
"""
    structured = {
        "metadata": {
            "class_name": "Class_6",
            "subject": "English",
            "exam_type": "Quarterly",
            "time_allowed": "2.5 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "All questions are compulsory.",
            "Write answers in a neat and legible hand."
        ],
        "sections": [
            {
                "title": "Question 1: Word Meanings (Any 10)",
                "questions": [
                    {"number": "1.", "text": "Write the Hindi meaning of <b>any ten</b> of the following words:<br/>"
                                              "<b>brave, country, insect, soldiers, favour, cattle, attack, prompt, impression, try, sparrows, village</b>",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 2: Fill in the Blanks",
                "questions": [
                    {"number": "2.", "text": "Fill in the blanks with the appropriate words given below:<br/>"
                                              "<b>[ tree, prompt, soldiers, worried, branches ]</b><br/>"
                                              "1. The teacher tried to __________________ Gandhiji during the inspection.<br/>"
                                              "2. King Bruce was very sad and __________________.<br/>"
                                              "3. The giant banyan tree spread its __________________ wide.<br/>"
                                              "4. Many of his brave __________________ were killed in the battle.<br/>"
                                              "5. I like the big mango __________________.",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 3: Column Matching",
                "questions": [
                    {"number": "3.", "text": "Match column 'A' with column 'B':<br/><br/>"
                                              "<table style='width: 75%; border-collapse: collapse; margin-left: 20px;'>"
                                              "<tr><th style='text-align: left;'><b>Column A</b></th><th style='text-align: left;'><b>Column B</b></th></tr>"
                                              "<tr><td>1. sad</td><td>— &nbsp; a fifty years old banyan tree</td></tr>"
                                              "<tr><td>2. The story is about</td><td>— &nbsp; swing on its branches</td></tr>"
                                              "<tr><td>3. The children</td><td>— &nbsp; sit under it to take rest</td></tr>"
                                              "<tr><td>4. The people</td><td>— &nbsp; take rest and sleep in it</td></tr>"
                                              "<tr><td>5. The birds</td><td>— &nbsp; happy</td></tr>"
                                              "</table>",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 4: True or False",
                "questions": [
                    {"number": "4.", "text": "Tick <b>[&check;]</b> for true and <b>[&cross;]</b> for false statements:<br/>"
                                              "1. The spider did not succeed in climbing up the wall. &nbsp;&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b><br/>"
                                              "2. It is a pleasant thing to sway in a swing. &nbsp;&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b><br/>"
                                              "3. It was a fifty years old mango tree. &nbsp;&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b><br/>"
                                              "4. Young Gandhiji misspelt the word 'kettle'. &nbsp;&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b><br/>"
                                              "5. Gandhiji left Porbandar at the age of eight. &nbsp;&nbsp; <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</b>",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 5: Short Answer Questions (Any 5)",
                "questions": [
                    {"number": "5.", "text": "Answer <b>any five</b> of the following questions:<br/>"
                                              "1. Where do we get pure fresh air from?<br/>"
                                              "2. What does the child see in the countryside from the swing?<br/>"
                                              "3. Who attacked King Bruce's country?<br/>"
                                              "4. When and where was Mahatma Gandhi born?<br/>"
                                              "5. What kind of ruler was King Bruce?<br/>"
                                              "6. What does the child see when he goes up in the air?",
                     "marks": "15", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 6: Application Writing",
                "questions": [
                    {"number": "6.", "text": "Write an application to the Principal of your school requesting <b>leave for three days</b> due to an urgent piece of work at home.",
                     "marks": "10", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured


# ==============================================================================
# 8. ENGLISH CLASS 8 (english 9.pdf)
# ==============================================================================
def get_paper_english_class8_transcription() -> Tuple[str, Dict[str, Any]]:
    raw_text = """Swami Pradeep Public School
Quarterly Examination - 2026-27
Class - 8th
Subject - English
Max Marks: 50 | Time: 2.5 Hours

1. Meanings (10 no.) (10 Marks):
Wish, another, mistakes, thrilling, Jeweller, peep, release, achieve, Excitement, give up

2. Match the columns (5 no.) (5 Marks):
woodcutter - one who cuts wood
exhausted - to set free
ornaments - thankless
ungrateful - jewellery
release - tired

3. Fill in the blanks (One Word Substitution) (5 no.) (5 Marks):
i. One who cuts wood - ______
ii. One who makes jewellery - ______
iii. One who saves others - ______
iv. One who travels - ______
v. One who makes sculptures - ______

4. Opposite Genders / Antonyms (10 no.) (10 Marks):
wife - madam - strong
father - king - actor
man - hot
son - happy

5. Answer the following questions (any 5) (15 Marks):
1. Why do we wish for another chance?
2. What was the challenge?
3. What is Kanha Kisli?
4. Where is it situated?
5. Who were trapped in the well?
6. What did the axemen do when the villagers hugged the trees and shouted 'chipko, chipko'?

6. Write an application for T.C. (Transfer Certificate) (5 Marks)
"""
    structured = {
        "metadata": {
            "class_name": "Class_8",
            "subject": "English",
            "exam_type": "Quarterly",
            "time_allowed": "2.5 Hours",
            "max_marks": "50"
        },
        "general_instructions": [
            "All questions are compulsory.",
            "Write answers clearly and mention proper question numbers."
        ],
        "sections": [
            {
                "title": "Question 1: Word Meanings",
                "questions": [
                    {"number": "1.", "text": "Write the Hindi meaning of the following words:<br/>"
                                              "<b>Wish, another, mistakes, thrilling, Jeweller, peep, release, achieve, Excitement, give up</b>",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 2: Vocabulary Matching",
                "questions": [
                    {"number": "2.", "text": "Match the words with their correct meanings:<br/><br/>"
                                              "<table style='width: 70%; border-collapse: collapse; margin-left: 20px;'>"
                                              "<tr><th style='text-align: left;'><b>Word</b></th><th style='text-align: left;'><b>Meaning</b></th></tr>"
                                              "<tr><td>woodcutter</td><td>— &nbsp; one who cuts wood</td></tr>"
                                              "<tr><td>exhausted</td><td>— &nbsp; tired</td></tr>"
                                              "<tr><td>ornaments</td><td>— &nbsp; jewellery</td></tr>"
                                              "<tr><td>ungrateful</td><td>— &nbsp; thankless</td></tr>"
                                              "<tr><td>release</td><td>— &nbsp; to set free</td></tr>"
                                              "</table>",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 3: One Word Substitution",
                "questions": [
                    {"number": "3.", "text": "Write one word for each of the following statements:<br/>"
                                              "(i) One who cuts wood in the forest &nbsp;&mdash;&nbsp; ____________________________________<br/>"
                                              "(ii) One who makes and sells ornaments &nbsp;&mdash;&nbsp; ____________________________________<br/>"
                                              "(iii) One who rescues and saves others &nbsp;&mdash;&nbsp; ____________________________________<br/>"
                                              "(iv) One who travels to different places &nbsp;&mdash;&nbsp; ____________________________________<br/>"
                                              "(v) One who carves statues and sculptures &nbsp;&mdash;&nbsp; ____________________________________",
                     "marks": "5", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 4: Gender & Opposites",
                "questions": [
                    {"number": "4.", "text": "Change the Gender or write Opposites as indicated:<br/>"
                                              "(i) <b>wife</b> &rarr; ____________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ii) <b>father</b> &rarr; ____________________<br/>"
                                              "(iii) <b>man</b> &rarr; ____________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (iv) <b>son</b> &rarr; ____________________<br/>"
                                              "(v) <b>madam</b> &rarr; ____________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (vi) <b>king</b> &rarr; ____________________<br/>"
                                              "(vii) <b>actor</b> &rarr; ____________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (viii) <b>hot</b> &times; ____________________<br/>"
                                              "(ix) <b>happy</b> &times; ____________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (x) <b>strong</b> &times; ____________________",
                     "marks": "10", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 5: Comprehension Questions (Any 5)",
                "questions": [
                    {"number": "5.", "text": "Answer <b>any five</b> of the following questions:<br/>"
                                              "1. Why do we wish for another chance in life?<br/>"
                                              "2. What was the challenge faced by the woodcutter?<br/>"
                                              "3. What is Kanha Kisli and why is it famous?<br/>"
                                              "4. Where is Kanha Kisli National Park situated?<br/>"
                                              "5. Who were trapped inside the deep well?<br/>"
                                              "6. What did the axemen do when the courageous villagers hugged the trees and shouted 'Chipko, Chipko'?",
                     "marks": "15", "is_or_choice": False}
                ]
            },
            {
                "title": "Question 6: Letter / Application Writing",
                "questions": [
                    {"number": "6.", "text": "Write an application to the Principal of your school requesting him/her to issue your <b>School Transfer Certificate (T.C.)</b>.",
                     "marks": "5", "is_or_choice": False}
                ]
            }
        ],
        "raw_transcription": raw_text
    }
    return raw_text, structured
