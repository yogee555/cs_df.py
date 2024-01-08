class besanth:
    course_inventory = {"python":10,"cloud_computing":10,"data_science":10}
    def greet(self):
        print("welcome to beasanth inventory")
    def course(self):
        for key,value in self.course_inventory.items():
            print(key,"---------",value)
    def enroll(self,subject):
        print(subject)
        for key, value in self.course_inventory.items():
            if key == subject:
                value = value -1
                self.course_inventory[key] = value
        print("congratulation you are successfully enrolled for",subject)
        print(self.course_inventory)

sudent1 = besanth()
sudent1.greet()
sudent1.course()
sudent1.enroll("python")
sandya = besanth()
sandya.greet()
sandya.course()
sandya.enroll("cloud_computing")
