import script_mod
import os
import sys

path = os.path.dirname(os.path.realpath(__file__))


def task(arg):
	if len(arg) > 1:
		options = dict(generate=generate, execute=execute)
		options[arg[1]]()
	else:
		print '****No arguements given. For help, type --> gen_sql.py help'


def generate():
	cred = script_mod.credentials.get_credentials(path)
	conn = script_mod.aws_con.connect_s3(cred)
	conn.connect_to_aws_bucket(cred['out_bucket'])
	store_list = conn.bucket.list()
	store_list_trimmed = script_mod.trim.trim_store_list(store_list)
	sql_script = script_mod.trim.generate_sql_new_tb(store_list_trimmed)
	# sql_script = script_mod.trim.generate_sql(store_list_trimmed)
	# sql_script = script_mod.trim.generate_sql_null_removed(store_list_trimmed)
	script_mod.trim.save_script(path, sql_script)


def execute():
	con = script_mod.postgre_con.connect_db()
	con.execute(script_mod.trim.get_script)
	con.commit()

if __name__ == '__main__':
	task(sys.argv)
