#-*- coding:utf-8 -*-
class DocstringClassExample():
	'''
	DocstringClassExample() 예제 클래스
	class에 대한 설명을 함께 적어준다.
	'''

	def docstring_func_example():
		"""
		Return 0 always
		"""
		print("ocstring_func_example 함수를 실행하였습니다.")
		return 0

def main():
	print("Docstring 만들어보기")
	new_doc = DocstringClassExample()
	print("Class docstring start")
	print(new_doc.__doc__)
	print("Class docstring end")
	print()
	print("Function docstring start")
	print(new_doc.docstring_func_example.__doc__)
	print("Function docstring end")


if __name__ == '__main__':
	main()