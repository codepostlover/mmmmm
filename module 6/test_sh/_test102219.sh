#!/bin/bash
 
function TestOutput {
    logs=${2:-""}
    logs=${logs//\"/\\\"}
    JSON_FMT='{"id":"%s","passed": %s, "log":"%s"}'
    printf "$JSON_FMT" "102219" $1 "$logs"  > ../outputs/102219.txt
}
 
# Write a bash script below
# It must call the function TestOutput <passed: true/false> <logs: string>
# For help getting started, click "Choose from template"
 
#!/bin/bash
 
i=$(python bookstore_input_generator.py)
 
student_output=$(python main.py < bookstore_input_0.txt)
expected_output=$(python mainCP.py < bookstore_input_0.txt)
shopt -s nocasematch
 
echo "$student_output"
echo "$expected_output"
 
echo "$student_output" | grep "Enter infix:" | sed 's/Enter infix: Enter structure (1 or 2): Enter max number of titles://'> student_titles.txt 
 
echo "$expected_output" | grep "Enter infix:" | sed 's/Enter infix: Enter structure (1 or 2): Enter max number of titles://'> expected_titles.txt
sed -i 's/^[[:space:]]*//; s/[[:space:]]*$//;s/[^[:alnum:]]//g' student_titles.txt
sed -i 's/^[[:space:]]*//; s/[[:space:]]*$//;s/[^[:alnum:]]//g' expected_titles.txt
 
cat student_titles.txt
cat expected_titles.txt
 
if diff student_titles.txt expected_titles.txt >/dev/null; then
  TestOutput true "$(cat feedback_0.txt)\nExpected:\n$(cat -n expected_titles.txt)\nReceived:\n$(cat -n student_titles.txt)"
 
else
  TestOutput false "$(cat feedback_0.txt)\nExpected:\n$(cat -n expected_titles.txt)\nReceived:\n$(cat -n student_titles.txt)"
fi
 