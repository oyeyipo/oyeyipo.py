from collections import namedtuple

fname = "Olawale"
lname = "Oyeyipo"
print(fname, lname)

Rec = namedtuple("Social", "Stackoverflow Github LinkedIn")
social = Rec(
    Stackoverflow="www.stackoverflow.com",
    Github="www.github.com/oyeyipo",
    LinkedIn="linkedin.com/oyeyipo",
)
