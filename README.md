

1.	Parsed data, return column names, data, and column index.
	def read_data(h1b_input)
	
2.	Counted certified applications that correspond to job title and state
	Return total_certified_apps, total_occupation, total_state.
	def total_columns

3. 	Ranked total occupation taking the certification application count
	Similarly for total state with the certification application count
	sorted in descending order and returned the top 10.
	def rank_data
	
4.	Wrote the top 10 occupations and percentage.
	def write_top10_ocupations
	
5.  Wrote the top states and percentage.
	def write_top10_states

6.  Assigned arguments and called all function. 
	def main(argv)
	
Run with Python3 and pass all tests.

 
Preferreds-Mac-mini:insight_testsuite Home$ ./run_tests.sh 
[ PASS ]: test_1 
[ PASS ]: test_1 top_10_states.txt
[Tue Oct 30 01:24:12 MDT 2018] 1 of 1 tests passed
Preferreds-Mac-mini:insight_testsuite Home$ more results.txt 
[Tue Oct 30 00:15:12 MDT 2018] 1 of 1 tests passed
[Tue Oct 30 00:17:46 MDT 2018] 1 of 1 tests passed
[Tue Oct 30 01:21:39 MDT 2018] 1 of 1 tests passed
[Tue Oct 30 01:24:12 MDT 2018] 1 of 1 tests passed
Preferreds-Mac-mini:insight_testsuite Home$ 