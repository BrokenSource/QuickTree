from attrs import define
from quicktree.tree.naive import NaiveTree


@define
class Event:
    name: str = ""
    desc: str = ""

tree = NaiveTree[Event]()
tree[ 0: 6] = Event("Early Morning")
tree[ 6:12] = Event("Morning")
tree[12:18] = Event("Afternoon")
tree[18:24] = Event("Night")
tree[ 0: 7] = Event("Sleeping")
tree[11:14] = Event("Lunch")

print("Crossing:")
for event in tree.cross(10.5, 12):
    print("•", event)

print("Inside:")
for event in tree.inside(10.5, 15):
    print("•", event)

print("At:")
for event in tree.at(16):
    print("•", event)
