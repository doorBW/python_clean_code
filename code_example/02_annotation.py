#-*- coding:utf-8 -*-
class AnnotationClassExample:
    """
    Annotation에 대한 예시를 확인하기 위한 class입니다.
    __annotation__ 속성을 통해
    class할당되는 first_param과 second_param에 대한 타입을 확인할 수 있습니다.
    """
    first_param: str
    second_param: int

    def set_first_param(self, value: str) -> None:
        """
        AnnotationClassExample 클래스의
        first_param 값을 바인딩합니다.
        함수의 반환은 없습니다.
        """
        self.first_param = value

    def set_second_param(self, value: int) -> bool:
        """
        AnnotationClassExample 클래스의
        second_param 값을 바인딩합니다.
        함수의 반환은 True or False 입니다.
        """
        if type(value) == int:
            self.second_param = value
            return True
        else:
            self.second_param = 0
            return False

def main():
    print("Annotation 만들어보기")
    new_class = AnnotationClassExample()
    print("\n* AnnotationClassExample 클래스의 annotations")
    print(new_class.__annotations__)
    print("\n* set_first_param 함수의 annotations")
    print(new_class.set_first_param.__annotations__)
    print("\n* set_second_param 함수의 annotations")
    print(new_class.set_second_param.__annotations__)

if __name__ == '__main__':
	main()