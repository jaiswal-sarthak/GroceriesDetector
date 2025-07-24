def count_objects(results, model):
    names = model.names
    detections = results[0].boxes.cls.tolist() if results[0].boxes is not None else []
    counts = {}

    for class_id in detections:
        label = names[int(class_id)]
        counts[label] = counts.get(label, 0) + 1

    return counts
