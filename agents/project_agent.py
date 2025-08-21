def project_agent(skills, all_projects, jd_text):
    """Simple text matching without scikit-learn dependency"""
    jd_words = set(jd_text.lower().split())
    
    # Score projects based on keyword overlap
    scored_projects = []
    for i, project in enumerate(all_projects):
        description = project.get("description", "").lower()
        tech_list = project.get("technologies", [])
        tech_text = " ".join(tech_list).lower()
        
        # Count keyword matches
        desc_words = set(description.split())
        tech_words = set(tech_text.split())
        all_proj_words = desc_words.union(tech_words)
        
        # Calculate simple overlap score
        score = len(jd_words.intersection(all_proj_words))
        
        # Bonus for project rating
        rating = project.get("rating", 0)
        score += rating * 2
        
        scored_projects.append((score, i, project))
    
    # Sort by score (descending) and return top 5
    scored_projects.sort(key=lambda x: x[0], reverse=True)
    return [proj[2] for proj in scored_projects[:5]]
