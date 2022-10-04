
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 밸류의 데이터 타입의 순서가 맞지않음
INSERT INTO zoo VALUES 
('gorilla','omnivore', 180, 210, 5);

-- 2)rowid는 행을 고유하게 식별해야하기 때문에 행마다 다른 값을 가져야함
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(11, 'alligator', 'carnivore', 250, 50);

-- 3) weight 가 not Null이기때문에 꼭 넣어줘야함
INSERT INTO zoo (name, eat, age, weight) VALUES
('dolphin', 'carnivore', 3,200);
