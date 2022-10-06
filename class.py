#クラスとは
class Person:
    #初期設定。必ず必要。
    #クラスを作る際は、必ず__init__関数を作成する必要があり、かつその中にselfを入れる必要がある。
    def __init__(self,name,nationality,age):
        self.name=name
        self.nationality=nationality
        self.age=age
    
    #__call__関数は、クラスの特殊な関数です。
    def __call__(self):
        print("ここはcall関数です。")
    
    def say_hello(self,name):
        print(f"こんにちは、{name}さん。私は{self.name}です。")

#インスタンス化(実体化)。クラスで決めた入力欄に入力するイメージ。
#ここでは、「今西」のオーダーメイドのプロフィールを作成している。
imanishi=Person("今西","日本",25)

#say_hello関数を呼ぶ。
imanishi.say_hello("佐藤")

#__call__関数の使い方。imanishi.__call__()としなくて良い。
imanishi()