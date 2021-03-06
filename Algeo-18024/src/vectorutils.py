import numpy as np


def euclidian_distance(v1, v2):
  """
  The euclidian function to count the distance between 2 vector
  For Magnitude distance
  """
  return np.sum((v1 - v2) ** 2)


def cosine_similarity(v1, v2):
  """
  Solving the cosine similarity between 2 vectors
  For orientation similarity
  """
  v1v2 = np.sum(v1 * v2)
  norm_v1_2 = np.sqrt(np.sum(v1 ** 2))
  norm_v2_2 = np.sqrt(np.sum(v2 ** 2))
  return v1v2 / (norm_v1_2 * norm_v2_2)
