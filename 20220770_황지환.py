class Node: # 단순 연결 리스트를 위한 노드 클래스
    def __init__(self, book_id, title, author, year, link=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.link = link

    def append(self, new): # 현재 노드 다음에 new 노드를 삽입
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self): # 현재 노드의 다음 노드를 삭제한 후 반환
        deleted_node = self.link
        if deleted_node is not None: self.link = deleted_node.link
        return deleted_node

class LinkedList: # 단순 연결 리스트 클래스
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, book_id, title, author, year): # 도서추가
        cur = self.head
        while cur is not None:
            if cur.book_id == book_id or cur.title == title:
                print(f"이미 등록된 도서입니다: '{title}' (번호 {book_id})\n")
                return
            cur = cur.link

        node = Node(book_id, title, author, year)
        if self.isEmpty():
            self.head = node
        else:
            cur = self.head
            while cur.link is not None: # 다음 노드가 존재 할때까지 반복
                cur = cur.link
            cur.append(node) # while 문으로 인해 현재 cur.link눈 none을 가리킴
        print(f"도서 '{title}'가 추가되었습니다\n")

    def find_by_title(self, title): #책 제목으로 리스트에서 도서를 찾기.
        cur = self.head
        while cur is not None: # 다음 노드가 존재 할때까지 반복
            if cur.title == title: 
                return cur
            cur = cur.link
        return None

    def find_pos_by_title(self, title): #책 제목으로 리스트에서 도서의 위치를 찾기
        cur = self.head
        index = 0
        while cur is not None: 
            if cur.title == title:
                return index
            cur = cur.link
            index += 1
        return -1

    def delete(self, title): #도서 삭제
        cur = self.head
        prev = None 
        while cur is not None: 
            if cur.title == title:
                if prev is None:
                    self.head = cur.link
                else:
                    prev.popNext()
                print(f"도서 '{title}'가 삭제되었습니다.\n")
                print("")
                return
            prev = cur
            cur = cur.link
        print(f"'{title}' 제목의 도서를 찾을 수 없습니다.\n")
        print("")

    def display(self): # 전체 도서 목록 출력
        if self.isEmpty():
            print("등록된 도서가 없습니다.\n")
            print("")
            return
        print("\n[전체 도서 목록]")
        cur = self.head
        while cur:
            print(f"책 번호 : {cur.book_id}, 제목 : {cur.title}, 저자 : {cur.author}, 출판 연도 : {cur.year}")
            cur = cur.link
        print("")


def menu():
        """메뉴 출력"""
        print("===   도서관리 프로그램   ===")
        print("1) 도서 추가")
        print("2) 도서 삭제 (책 제목으로 삭제)")
        print("3) 도서 조회 (책 제목으로 조회)")
        print("4) 전체 도서 목록 출력")
        print("5) 프로그램 종료")


def main():
    """메인 함수"""
    lb = LinkedList()
    while True:
        menu()
        cc = input("메뉴를 선택하세요: ").strip().lower()

        if cc == "1":
            book_number = input("책 번호를 입력하세요 : ")
            book_name = input("책 제목을 입력하세요 : ")
            book_author = input("저자를 입력하세요 : ")
            book_year = input("출판 연도를 입력하세요 : ")
            lb.insert(book_number, book_name, book_author, book_year)

        elif cc == "2":
            book_delete = input("삭제할 책 제목을 입력하세요 : ")
            lb.delete(book_delete)

        elif cc == "3":
            book_name = input("조회할 책 제목을 입력하세요 : ")
            found = lb.find_by_title(book_name)
            if found:
                print("\n[도서 정보]")
                print(f"번호: {found.book_id}")
                print(f"제목: {found.title}")
                print(f"저자: {found.author}")
                print(f"출판연도: {found.year}\n")
            else:
                print(f"'{book_name}' 제목의 도서를 찾을 수 없습니다.\n")

        elif cc == "4":
            lb.display()

        elif cc == "5":
            print("종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 입력해주세요\n")

if __name__ == "__main__":
    main()