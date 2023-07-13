-- Creates a stored procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE total_score FLOAT;
	DECLARE count_scores INT;
	DECLARE avg_score FLOAT;


	-- Compute the total score for the user
	SELECT SUM(score) INTO total_score
	FROM corrections
	WHERE user_id = user_id;

	-- Count the number of scores for the user
	SELECT COUNT(*) INTO count_scores
	FROM corrections
	WHERE user_id = user_id;

	-- Compute the average score
	IF count_scores > 0 THEN
	    SET avg_score = total_score / count_scores;
	ELSE
	    SET avg_score = 0;
	END IF;

	-- Update the average_score column for the user
	UPDATE users
	SET average_score = avg_score
	WHERE id = user_id;
END //

DELIMITER ;
