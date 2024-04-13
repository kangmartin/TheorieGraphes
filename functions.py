def lire_taches_fichier(filename):
    tasks = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            # Rajouter une liste s'il y a des prédécesseurs
            if len(parts) > 1:
                task_id = int(parts[0])
                duration = int(parts[1])
                predecessors = [int(x) for x in parts[2:]] if len(parts) > 2 else []
                tasks.append((task_id, duration, predecessors))
    return tasks


def calcul_sommets(tasks):
    # Nombre de tâches + 2 pour les sommets fictifs α (0) et ω (N+1)
    sommets_count = len(tasks) + 2
    return sommets_count


def calcul_arc(tasks):
    arc_count = 0
    has_predecessors = set()
    all_tasks = set()

    # Compter les arcs en fonction des prédécesseurs
    for task_id, _, predecessors in tasks:
        all_tasks.add(task_id)
        if predecessors:
            arc_count += len(predecessors)
            has_predecessors.update(predecessors)
        else:
            # Tâche sans prédécesseur, un arc depuis alpha
            arc_count += 1

    # Ajouter un arc vers ω pour les tâches sans successeurs
    no_successors = all_tasks - has_predecessors
    arc_count += len(no_successors)
    return arc_count


def afficher_graph(tasks):
    print("Le fichier à:", calcul_sommets(tasks), "sommets")
    print("Le fichier à:", calcul_arc(tasks), "arcs")
    pred = []
    for i in tasks:
        pred.append(i[2])
    for j in range(len(pred)):
        if len(pred[j]) == 0:
            print("0 ->", tasks[j][0], "= 0")
        else:
            for z in range(len(pred[j])):
                print(pred[j][z], "->", tasks[j][0], "=", tasks[pred[j][z] - 1][1])

    all_tasks = set(task[0] for task in tasks)
    tasks_with_predecessors = set(pred for task in tasks for pred in task[2])
    tasks_without_successors = all_tasks - tasks_with_predecessors
    omega = max(all_tasks) + 1
    for task in tasks:
        if task[0] in tasks_without_successors:
            print(task[0], "->", omega, "=", task[1])
