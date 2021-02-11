from typing import Dict, List, Optional, Set, Tuple


class Node:
    def __init__(self, nid: int,
                 name: str,
                 owner: str,
                 is_dir: bool,
                 size: int,
                 parent: Optional['Node'],
                 children: List['Node']) -> None:
        self.nid = nid
        self.name = name
        self.owner = owner
        self.is_dir = is_dir
        self.size = size
        self.parent = parent
        self.children = children

    def is_valid_helper(self) -> bool:
        if (self.parent and not self.name) or '/' in self.name:
            return False
        if not self.owner:
            return False
        if self.children:
            names = []
            for child in self.children:
                names.append(child.name)
            if len(names) != len(set(names)):
                return False
        if self.children:
            for child in self.children:
                if Node.is_valid_helper(child) is False:
                    return False
        return True

    def koren_finder(self) -> 'Node':
        x = self
        while x.parent:
            x = x.parent
        return x

    def is_valid(self) -> bool:
        return Node.is_valid_helper(Node.koren_finder(self))

    def draw_helper(self, final_parent: Optional['Node'], check: bool) -> None:
        magic = []
        result = ''
        if check is True:
            print('-- ' + self.name)
        else:
            space = '    '
            dir_space = '   |'
            end_space = '   \\'
            i = self
            count = 0
            while i.parent != final_parent:
                if i.parent:
                    if i.parent.children[len(i.parent.children) - 1] \
                            == i and count == 0:
                        magic.append(end_space)
                    elif i.parent.children[len(i.parent.children) - 1] \
                            != i and len(i.parent.children) > 1:
                        magic.append(dir_space)
                    else:
                        magic.append(space)
                    i = i.parent
                    count += 1
            magic.reverse()
            for every in magic:
                result += every

            print(result + '-- ' + self.name)
        if self.children:
            for child in self.children:
                Node.draw_helper(child, final_parent, False)

    def draw(self) -> None:
        if self.parent:
            final_parent: Node = self.parent
            Node.draw_helper(self, final_parent, True)
        else:
            Node.draw_helper(self, None, True)

    def full_path(self) -> str:
        result = ''
        x = self
        while x.parent:
            result = '/' + x.name + result
            x = x.parent
        if self.is_dir is True:
            result += '/'
        return result

    def disk_usage(self) -> Tuple[int, int]:
        count = 0
        size = 0
        if self.is_dir is False:
            size += self.size
            count += 1
        if self.children:
            for child in self.children:
                if child.is_dir is True and child.children:
                    result = Node.disk_usage(child)
                    count += result[0]
                    size += result[1]
                elif child.is_dir is False:
                    size += child.size
                    count += 1
        return count, size

    def owners_helper(self) -> List[str]:
        result = [self.owner]
        if self.children:
            for child in self.children:
                x = Node.owners_helper(child)
                for every in x:
                    result.append(every)
        return result

    def all_owners(self) -> Set[str]:
        return set(Node.owners_helper(self))

    def empty_helper(self) -> List['Node']:
        result = []
        if self.size == 0 and self.is_dir is False:
            result.append(self)
        if self.children:
            for child in self.children:
                x = Node.empty_helper(child)
                for i in x:
                    result.append(i)
        return result

    def empty_files(self) -> List['Node']:
        return Node.empty_helper(self)

    def prepend_owner_name(self) -> None:
        if self.is_dir is False:
            self.name = self.owner + '_' + self.name
        if self.children:
            for child in self.children:
                Node.prepend_owner_name(child)

    def keep_helper(self, start: int) -> List[int]:
        result = []
        if self.children:
            for child in self.children:
                x = Node.keep_helper(child, start)
                for i in x:
                    result.append(i)
        if self.name == '.keep' \
                and self.is_dir is False \
                and self.nid >= start:
            result.append(self.nid)
        return result

    def add_keep_files(self, start: int) -> None:
        num = start
        if self.is_dir is True and not self.children:
            koren = Node.koren_finder(self)
            list_of_nid = Node.keep_helper(koren, start)
            if len(list_of_nid) == 0:
                self.children.append(Node
                                     (num, '.keep',
                                      self.owner, False,
                                      0, self, []))
            else:
                self.children.append(Node
                                     (int(max(list_of_nid)) + 1,
                                      '.keep',
                                      self.owner, False, 0,
                                      self, []))
        if self.children:
            for child in self.children:
                Node.add_keep_files(child, num)

    def is_empty_dirs(self) -> List[bool]:
        result: List[bool] = []
        is_dir_empty = False
        if not self.children and self.is_dir is True:
            is_dir_empty = True
        else:
            for child in self.children:
                x = Node.is_empty_dirs(child)
                for i in x:
                    result.append(i)
        result.append(is_dir_empty)
        return result

    def remove_helper(self) -> None:
        new_child: List['Node'] = []

        if self.parent and self.is_dir is True and not self.children:
            for ch in self.parent.children:
                if ch != self:
                    new_child.append(ch)
            self.parent.children = new_child

        if self.children:
            for child in self.children:
                Node.remove_helper(child)

    def remove_empty_dirs(self) -> None:
        if self.children:

            if Node.disk_usage(self) == (0, 0):
                self.children = []
            elif any(Node.is_empty_dirs(self)):
                while any(Node.is_empty_dirs(self)):
                    Node.remove_helper(self)

    def foreign_helper(self, user: str, final_parent: Optional['Node']) \
            -> None:
        new_children: List['Node'] = []
        if self.parent \
                and self.owner != user \
                and self.parent != final_parent:
            if self in self.parent.children:

                # if i understood
                for ch in self.parent.children:
                    if ch != self:
                        new_children.append(ch)
                self.parent.children = new_children

                self.children = []
        if self.children:
            for child in self.children:
                Node.foreign_helper(child, user, final_parent)

    def remove_all_foreign(self, user: str) -> None:
        final_parent: Optional['Node'] = None
        if self.parent:
            final_parent = self.parent
        if user not in Node.all_owners(self):
            self.children = []
        if self.children and Node.all_owners(self) != {user}:
            for child in self.children:
                while child and child.parent and \
                        child in child.parent.children \
                        and Node.all_owners(child) != {user}:
                    Node.foreign_helper(self, user, final_parent)
        for new_child in self.children:
            if Node.all_owners(new_child) != {user}:
                Node.remove_all_foreign(self, user)


def build_helper(just_num: int, const_key: int,
                 metadata: Dict[int, Tuple[str, str]],
                 file_sizes: Dict[int, int],
                 dir_content: Dict[int, List[int]]) -> Optional[Node]:
    nid = just_num
    name = metadata[nid][0]
    owner = metadata[nid][1]
    is_dir = True
    size = 0
    children: List['Node'] = []
    parent = None
    if nid in list(dir_content.keys()):
        if dir_content.values():
            for i in dir_content[nid]:
                x = build_helper(i, const_key, metadata,
                                 file_sizes, dir_content)
                if x:
                    new_child: Node = x
                    children.append(new_child)
    if nid in file_sizes.keys():
        is_dir = False
        size = int(file_sizes[nid])
    result: Node = Node(nid, name, owner, is_dir, size, parent, children)
    if result.children:
        for child in result.children:
            child.parent = result

    return result


def build_checker(metadata: Dict[int, Tuple[str, str]],
                  file_sizes: Dict[int, int],
                  dir_content: Dict[int, List[int]]) -> Tuple[bool, int]:
    meta_nid: List[int] = list(metadata.keys())
    sizes_nid: List[int] = list(file_sizes.keys())
    parent_nid: List[int] = list(dir_content.keys())
    children_nid: List[int] = sum(list(dir_content.values()), [])
    dir_content_nid: List[int] = list(set(parent_nid + children_nid))
    koren_nid: int = 0
    if set(dir_content_nid + sizes_nid) - set(meta_nid):
        return False, koren_nid
    if len(set(parent_nid) & set(sizes_nid)) > 0:
        return False, koren_nid
    if set(dir_content_nid + sizes_nid) & set(meta_nid) != set(meta_nid) \
            and (len(meta_nid) != 1 and
                 len(sizes_nid) != 0 and
                 len(dir_content_nid) != 0):
        return False, koren_nid
    x = list(set(meta_nid) - set(children_nid))
    if len(x) != 1:
        return False, koren_nid
    else:
        koren_nid = x[0]
    return True, koren_nid


def build_fs(metadata: Dict[int, Tuple[str, str]],
             file_sizes: Dict[int, int],
             dir_content: Dict[int, List[int]]) -> Optional[Node]:
    if not metadata:
        return None
    x = build_checker(metadata,
                      file_sizes,
                      dir_content)
    if not x[0]:
        return None
    key = const_key = x[1]
    return build_helper(key, const_key, metadata, file_sizes,
                        dir_content)


def test_root_only() -> None:
    root = build_fs({1: ("", "root")}, {}, {})
    assert root is not None
    assert root.nid == 1
    assert root.name == ""
    assert root.owner == "root"
    assert root.is_dir
    assert root.size == 0
    assert root.parent is None
    assert root.children == []
    assert root.is_valid()
    assert root.full_path() == "/"
    assert root.disk_usage() == (0, 0)
    assert root.all_owners() == {"root"}
    assert root.empty_files() == []


def test_example() -> None:

    root = example_fs()
    assert root is not None
    assert root.name == 'MY_FS'
    assert root.owner == 'root'
    home = root.children[2]
    assert home.name == 'home'
    assert home.owner == 'root'
    ib111 = home.children[0].children[0]
    assert ib111.name == 'ib111'
    assert ib111.owner == 'user'
    assert ib111.is_dir

    assert len(ib111.children[0].children) == 4
    python = root.children[0].children[1]
    assert python.name == 'python'
    assert python.owner == 'root'
    assert python.size == 14088
    assert not python.is_dir
    assert root.children[3].is_dir

    assert ib111.parent is not None
    assert ib111.parent.parent == home

    assert ib111.is_valid()
    assert python.is_valid()
    python.name = ""
    assert not ib111.is_valid()
    python.name = "python"

    assert python.full_path() == '/bin/python'
    assert ib111.children[0].full_path() == '/home/user/ib111/reviews/'

    assert root.disk_usage() == (8, 1210022)
    assert home.disk_usage() == (4, 78326)

    assert root.all_owners() == {'nobody', 'user', 'root'}
    assert home.all_owners() == {'user', 'root'}
    assert python.all_owners() == {'root'}

    empty = ib111.children[0].children[3]
    assert empty.name == '.timestamp'
    assert root.empty_files() == [empty]

    root.prepend_owner_name()
    assert python.name == 'root_python'
    assert empty.name == 'user_.timestamp'

    root.add_keep_files(7000)

    keep1 = root.children[-1].children[0]
    assert keep1.name == '.keep'
    assert keep1.size == 0
    assert not keep1.is_dir

    keep2 = home.children[0].children[1].children[0].children[0]
    assert keep2.name == '.keep'
    assert keep2.size == 0
    assert not keep2.is_dir

    empty_files = root.empty_files()
    assert len(empty_files) == 3
    assert empty in empty_files
    assert keep1 in empty_files
    assert keep2 in empty_files
    assert keep1.nid + keep2.nid == 7000 + 7001


def draw_example() -> None:
    root = example_fs()
    print("První příklad:")
    root.draw()
    print("\nDruhý příklad:")
    root.children[2].draw()

    print("\nPrvní příklad, po použití root.remove_empty_dirs():")
    root = example_fs()
    root.remove_empty_dirs()
    root.draw()

    print("\nPrvní příklad, po použití root.remove_all_foreign('root'):")
    root = example_fs()
    root.remove_all_foreign('root')
    root.draw()

    print("\nPrvní příklad, po použití root.remove_all_foreign('nobody'):")
    root = example_fs()
    root.children[0].remove_all_foreign('nobody')
    root.remove_all_foreign('nobody')
    root.draw()


def example_fs() -> Node:
    root = build_fs(
        {
            1: ("MY_FS", "root"),
            17: ("bash", "root"),
            42: ("bin", "root"),
            9: ("ls", "root"),
            11: ("python", "root"),
            20: ("usr", "root"),
            1007: ("bin", "root"),
            1100: ("env", "root"),
            999: ("home", "root"),
            2001: ("ib111", "user"),
            25: ("user", "user"),
            2002: ("reviews", "user"),
            3000: ("review1.txt", "user"),
            3017: ("review2.txt", "user"),
            3005: ("review3.txt", "user"),
            100: ("tmp", "nobody"),
            2003: ("pv264", "user"),
            3001: ("projects", "user"),
            1234: (".timestamp", "user"),
        },
        {
            9: 141936,
            11: 14088,
            1100: 47656,
            17: 928016,
            3000: 11660,
            3017: 12345,
            3005: 54321,
            1234: 0,
        },
        {
            1: [42, 20, 999, 100],
            42: [9, 11, 17],
            20: [1007],
            1007: [1100],
            999: [25],
            25: [2001, 2003],
            2001: [2002],
            2002: [3000, 3017, 3005, 1234],
            2003: [3001],
        })
    assert root is not None
    return root


if __name__ == '__main__':
    test_root_only()
    test_example()
    draw_example()  # uncomment to run
