def best(field, workingPieces, workingPieceIndex, weights, level):
        bestRotation = None
        bestOffset = None
        bestScore = None
        workingPieceIndex = copy.deepcopy(workingPieceIndex)
        workingPiece = workingPieces[workingPieceIndex]
        shapes_rotation = { 4 : 4, 8 : 2, 12 : 2, 16 : 4, 20 : 4, 24 : 2, 28 : 1 }
        flat_piece = [val for sublist in workingPiece for val in sublist]
        hashedPiece = sum(flat_piece)

        for rotation in range(0, shapes_rotation[hashedPiece]):
            for offset in range(0, field.width):
                result = field.projectPieceDown(workingPiece, offset, level)
                if not result is None:
                    score = None
                    if workingPieceIndex == len(workingPieces)-1 :
                        heuristics = field.heuristics()
                        score = sum([a*b for a,b in zip(heuristics, weights)])
                    else:
                        _, _, score = Ai.best(field, workingPieces, workingPieceIndex + 1, weights, 2)

                    if bestScore is None or score > bestScore:
                        bestScore = score
                        bestOffset = offset
                        bestRotation = rotation
                field.undo(level)
            workingPiece = rotate_clockwise(workingPiece)

        return bestOffset, bestRotation, bestScore





def minimax(tetris, depth, player):
	if player == MAX:
		best = [-1, -1, -infinity]
	else:
		best = [-1, -1, +infinity]

	if depth == 0 or tetris.gameover:
		score = evaluate(tetris)
		return [-1, -1, score]

  shapes_rotation = { 4 : 4, 8 : 2, 12 : 2, 16 : 4, 20 : 4, 24 : 2, 28 : 1 }
  workingPieceIndex = copy.deepcopy(workingPieceIndex)
  workingPiece = workingPieces[workingPieceIndex]
  flat_piece = [val for sublist in workingPiece for val in sublist]
  hashedPiece = sum(flat_piece)
  
	for rotation in range(0, shapes_rotation[hashedPiece]):
            for offset in range(0, field.width):
                result = field.projectPieceDown(workingPiece, offset, level)
                if not result is None:
                    score = None
                    if workingPieceIndex == len(workingPieces)-1 :
                        heuristics = field.heuristics()
                        score = sum([a*b for a,b in zip(heuristics, weights)])
                    else:
                        _, _, score = Ai.best(field, workingPieces, workingPieceIndex + 1, weights, 2)

                    if bestScore is None or score > bestScore:
                        bestScore = score
                        bestOffset = offset
                        bestRotation = rotation
                field.undo(level)
            workingPiece = rotate_clockwise(workingPiece)

	return best