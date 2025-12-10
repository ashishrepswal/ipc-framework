# acl.py - simple ACL stub
class ACL:
    def __init__(self):
        self.allowed = set()

    def allow(self, uid):
        self.allowed.add(uid)

    def deny(self, uid):
        if uid in self.allowed:
            self.allowed.remove(uid)

    def check(self, uid):
        return uid in self.allowed

if __name__ == '__main__':
    a = ACL()
    a.allow(1000)
    print('check 1000:', a.check(1000))
    print('check 2000:', a.check(2000))
