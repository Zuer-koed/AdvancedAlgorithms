from graph import Graph
from person import Person


def create_initial_profiles():
    """
    Create initial 5-10 Person profiles for the social media app.
    Returns a list of Person objects.
    """
    people = [
        Person("Zuer", "Female", "Love traveling and photography", "public"),
        Person("Haoxiang", "Male", "Tech enthusiast and gamer", "public"),
        Person("Shaun", "Male", "Fitness trainer and motivator", "private"),
        Person("Luyao", "Female", "Food blogger and chef", "public"),
        Person("Feii", "Female", "Book lover and writer", "private"),
        Person("Hang Yi", "Male", "Music producer and DJ", "public"),
        Person("Xuan", "Female", "Environmental activist", "private")
    ]
    return people


def setup_social_graph(people):
    """
    Set up the social graph with follow relationships.
    Returns a Graph object with people and relationships.
    """
    social_graph = Graph()

    # Add all people to the graph as vertices
    for person in people:
        social_graph.add_vertex(person)

    # Create follow relationships (mimic Instagram)
    # Alice's follows
    social_graph.add_edge(people[0], people[1])  # Alice follows Bob
    social_graph.add_edge(people[0], people[3])  # Alice follows Diana
    social_graph.add_edge(people[0], people[6])  # Alice follows Grace

    # Bob's follows
    social_graph.add_edge(people[1], people[0])  # Bob follows Alice
    social_graph.add_edge(people[1], people[2])  # Bob follows Charlie
    social_graph.add_edge(people[1], people[4])  # Bob follows Eve

    # Charlie's follows
    social_graph.add_edge(people[2], people[3])  # Charlie follows Diana
    social_graph.add_edge(people[2], people[5])  # Charlie follows Frank

    # Diana's follows
    social_graph.add_edge(people[3], people[0])  # Diana follows Alice
    social_graph.add_edge(people[3], people[6])  # Diana follows Grace

    # Eve's follows
    social_graph.add_edge(people[4], people[1])  # Eve follows Bob
    social_graph.add_edge(people[4], people[5])  # Eve follows Frank

    # Frank's follows
    social_graph.add_edge(people[5], people[2])  # Frank follows Charlie
    social_graph.add_edge(people[5], people[4])  # Frank follows Eve

    # Grace's follows
    social_graph.add_edge(people[6], people[0])  # Grace follows Alice
    social_graph.add_edge(people[6], people[3])  # Grace follows Diana

    return social_graph


def find_person_by_name(people, name):
    """
    Find a person by name in the list of people.
    """
    for person in people:
        if person.name.lower() == name.lower():
            return person
    return None


def display_all_users(people):
    """1. Display all users' names"""
    print("\n--- All Users ---")
    for i, person in enumerate(people, 1):
        print(f"{i}. {person.name}")


def view_user_profile(people):
    """2. View profile of any person in detail"""
    name = input("Enter the name of the person: ").strip()
    person = find_person_by_name(people, name)

    if person:
        person.display_profile()
    else:
        print("User not found!")


def view_followed_accounts(social_graph, people):
    """3. View followed accounts of a particular person"""
    name = input("Enter the name of the person: ").strip()
    person = find_person_by_name(people, name)

    if person:
        following = social_graph.list_outgoing_adjacent_vertex(person)
        if following:
            print(f"\n{name} follows:")
            for followed_person in following:
                print(f"- {followed_person.name}")
        else:
            print(f"{name} is not following anyone.")
    else:
        print("User not found!")


def view_followers(social_graph, people):
    """4. View followers of a particular person"""
    name = input("Enter the name of the person: ").strip()
    person = find_person_by_name(people, name)

    if person:
        # Find all people who follow this person
        followers = []
        for user in people:
            following = social_graph.list_outgoing_adjacent_vertex(user)
            if person in following:
                followers.append(user)

        if followers:
            print(f"\nFollowers of {name}:")
            for follower in followers:
                print(f"- {follower.name}")
        else:
            print(f"{name} has no followers.")
    else:
        print("User not found!")


def add_new_user(social_graph, people):
    """5a. Add user profile on-demand"""
    print("\n--- Add New User ---")
    name = input("Enter new user's name: ").strip()

    # Check if user already exists
    if find_person_by_name(people, name):
        print("User already exists!")
        return

    gender = input("Enter gender: ").strip()
    biography = input("Enter biography: ").strip()
    privacy = input("Enter privacy (public/private): ").strip().lower()

    if privacy not in ['public', 'private']:
        print("Privacy must be 'public' or 'private'! Defaulting to public.")
        privacy = 'public'

    new_person = Person(name, gender, biography, privacy)
    people.append(new_person)
    social_graph.add_vertex(new_person)

    print(f"User '{name}' added successfully!")


def follow_user(social_graph, people):
    """5c. Follow another user on-demand"""
    print("\n--- Follow User ---")
    follower_name = input("Who wants to follow? ").strip()
    followee_name = input("Who to follow? ").strip()

    follower = find_person_by_name(people, follower_name)
    followee = find_person_by_name(people, followee_name)

    if not follower:
        print(f"User '{follower_name}' not found!")
        return
    if not followee:
        print(f"User '{followee_name}' not found!")
        return

    if social_graph.add_edge(follower, followee):
        print(f"{follower_name} now follows {followee_name}!")
    else:
        print(f"{follower_name} already follows {followee_name}!")


def unfollow_user(social_graph, people):
    """5d. Unfollow a user on-demand"""
    print("\n--- Unfollow User ---")
    unfollower_name = input("Who wants to unfollow? ").strip()
    unfollowee_name = input("Who to unfollow? ").strip()

    unfollower = find_person_by_name(people, unfollower_name)
    unfollowee = find_person_by_name(people, unfollowee_name)

    if not unfollower:
        print(f"User '{unfollower_name}' not found!")
        return
    if not unfollowee:
        print(f"User '{unfollowee_name}' not found!")
        return

    if social_graph.remove_edge(unfollower, unfollowee):
        print(f"{unfollower_name} unfollowed {unfollowee_name}!")
    else:
        print(f"{unfollower_name} doesn't follow {unfollowee_name}!")


def main_menu(social_graph, people):
    """Main menu system with all features"""
    while True:
        print("\n" + "=" * 40)
        print("       SOCIAL MEDIA MENU")
        print("=" * 40)
        print("1. Display all users")
        print("2. View user profile")
        print("3. View followed accounts")
        print("4. View followers")
        print("5. Add new user")
        print("6. Follow user")
        print("7. Unfollow user")
        print("8. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            display_all_users(people)
        elif choice == "2":
            view_user_profile(people)
        elif choice == "3":
            view_followed_accounts(social_graph, people)
        elif choice == "4":
            view_followers(social_graph, people)
        elif choice == "5":
            add_new_user(social_graph, people)
        elif choice == "6":
            follow_user(social_graph, people)
        elif choice == "7":
            unfollow_user(social_graph, people)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-8.")


if __name__ == "__main__":
    print("=" * 50)
    print("       SOCIAL MEDIA NETWORK")
    print("=" * 50)

    # Setup
    people = create_initial_profiles()
    social_graph = setup_social_graph(people)

    print("✓ System ready! 7 users loaded.")

    # Start menu
    main_menu(social_graph, people)