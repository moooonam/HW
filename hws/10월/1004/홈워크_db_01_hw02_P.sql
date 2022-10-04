CREATE TABLE zoo_2 (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo_2 VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

BEGIN;
  DELETE FROM zoo_2
  WHERE weight < 100;
ROLLBACK;

BEGIN;
  DELETE FROM zoo_2
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo_2;
-- 롤백을 한 부분은 실행을 했다가 다시 되돌렸기 때문에 적용이 안된거나 마찬가지고 밑에 COMMIT을 한 부분은 eat가 'omnivore'인 레코드를 삭제했기 때문에 데이터에는 tiger,elephant,panda만 남는다 