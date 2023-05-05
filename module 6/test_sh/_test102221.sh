#!/bin/bash
 
function TestOutput {
    logs=${2:-""}
    logs=${logs//\"/\\\"}
    JSON_FMT='{"id":"%s","passed": %s, "log":"%s"}'
    printf "$JSON_FMT" "102221" $1 "$logs"  > ../outputs/102221.txt
}
 
# Write a bash script below
# It must call the function TestOutput <passed: true/false> <logs: string>
# For help getting started, click "Choose from template"
#!/bin/bash
 
i=$(python bookstore_input_generator.py)
 
student_output=$(python main.py < bookstore_input_3.txt)
expected_output=$(python mainCP.py < bookstore_input_3.txt)
shopt -s nocasematch
echo "$student_output"
 
 
echo "$student_output" | grep "Book:"> student_books.txt 
 
echo "$expected_output" | grep "Book:"> expected_books.txt
 
echo "$student_output" | grep "Title:"> student_titles.txt 
 
echo "$expected_output" | grep "Title:"> expected_titles.txt
sed -i 's/^[[:space:]]*//; s/[[:space:]]*$//' student_titles.txt
sed -i 's/^[[:space:]]*//; s/[[:space:]]*$//' expected_titles.txt
sed -i 's/^[[:space:]]*//; s/[[:space:]]*$//' student_books.txt
sed -i 's/^[[:space:]]*//; s/[[:space:]]*$//' expected_books.txt
 
cat student_books.txt
cat student_titles.txt
if grep "Title:" student_titles.txt >/dev/null && grep "Book:" student_books.txt >/dev/null; then
  if diff student_books.txt expected_books.txt >/dev/null; then
      TestOutput true "$(cat feedback_3.txt)\nExpected:\n$(cat -n expected_titles.txt)\nReceived:\n$(cat -n student_titles.txt)"
  else
      TestOutput false "$(cat feedback_3.txt)\nExpected:\n$(cat -n expected_titles.txt)\nReceived:\n$(cat -n student_titles.txt)"
  fi
else
	TestOutput false "$(cat feedback_3.txt)\nExpected:\n$(cat -n expected_titles.txt)\nReceived:\n$(cat -n student_titles.txt)"
    exit 1
fi
 
 