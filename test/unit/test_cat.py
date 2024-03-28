from models.cat_model import Cat

def test_cat():
    """
    GIVEN a Cat model
    WHEN a new Cat is created
    THEN check the name, image path
    """
    cat = Cat(20, "mittens", "public/img/cats/mittens.jpg")
    assert cat.id == 20
    assert cat.name == "mittens"
    assert cat.path == "public/img/cats/mittens.jpg"