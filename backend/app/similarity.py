import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict

class JobSimilarityEngine:
    def __init__(self, data_loader):
        self.data_loader = data_loader

    def find_similar_jobs(self, job_data: Dict, top_k: int = 5) -> List[Dict]:
        """Find similar jobs with lower risk scores"""
        current_vector = np.array(job_data["skill_vector"]).reshape(1, -1)
        current_risk = job_data["risk_score"]

        all_jobs = self.data_loader.get_all_jobs()
        candidates = []

        for job in all_jobs:
            if job["title"] == job_data["title"]:
                continue

            # Only suggest safer jobs
            if job["risk_score"] >= current_risk:
                continue

            job_vector = np.array(job["skill_vector"]).reshape(1, -1)
            similarity = cosine_similarity(current_vector, job_vector)[0][0]

            candidates.append({
                "title": job["title"],
                "risk_score": job["risk_score"],
                "similarity": float(similarity),
                "risk_reduction": current_risk - job["risk_score"]
            })

        # Sort by similarity, then risk reduction
        candidates.sort(key=lambda x: (x["similarity"], x["risk_reduction"]), reverse=True)
        return candidates[:top_k]

    def calculate_skill_gap(self, current_job: Dict, target_job: Dict) -> List[str]:
        """Identify skills to learn for pivot"""
        current_skills = set(current_job["skills"])
        target_skills = set(target_job["skills"])
        return list(target_skills - current_skills)
