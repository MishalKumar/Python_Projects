class TreeNode:
    # Individual node of tree
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    # adding child node inside tree
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    #get level of tree node
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 10
        prefix = spaces + "--symptom--" if (self.parent) else ''
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()

# Symptoms tree

def create_symptoms_tree():
    root = TreeNode("Root")

    Abdominal_pain = TreeNode("Abdominal pain")

    Abdominal_pain.add_child(TreeNode("--location--Abdominal pain, right upper quadrant"))
    Abdominal_pain.add_child(TreeNode("--location--Abdominal pain, right lower quadrant"))
    Abdominal_pain.add_child(TreeNode("--location--Abdominal pain, left upper quadrant"))
    Abdominal_pain.add_child(TreeNode("--location--Abdominal pain, right upper quadrant"))
    Abdominal_pain.add_child(TreeNode("--severity--Abdominal pain, mild"))
    Abdominal_pain.add_child(TreeNode("--severity--Abdominal pain, moderate"))
    Abdominal_pain.add_child(TreeNode("--severity--Abdominal pain, severe"))

    Chest_pain = TreeNode("Chest pain")
    Chest_pain.add_child(TreeNode("--location--Chest pain, left side"))
    Chest_pain.add_child(TreeNode("--location--Chest pain, right side"))
    Chest_pain.add_child(TreeNode("--severity--Chest pain, mild"))
    Chest_pain.add_child(TreeNode("--severity--Chest pain, moderate"))
    Chest_pain.add_child(TreeNode("--severity--Chest pain, severe"))

    root.add_child(Abdominal_pain)
    root.add_child(Chest_pain)
    # print(Chest_pain.get_level())
    return root

if __name__ == '__main__':
    root = create_symptoms_tree()
    # print(root)
    print(root.print_tree())
    # print(root.get_level())