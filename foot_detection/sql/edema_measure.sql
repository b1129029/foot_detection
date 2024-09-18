CREATE TABLE `水腫程度` (
  `測量編號` TEXT NOT NULL,
  `病患_ID` TEXT DEFAULT NULL,
  `測量時間` TEXT DEFAULT NULL,
  `腳圍` FLOAT DEFAULT NULL,
  PRIMARY KEY (`測量編號`),
  FOREIGN KEY (`病患_ID`) REFERENCES `病患資料` (`病患_ID`)
);

INSERT INTO `水腫程度` (`測量編號`, `病患_ID`, `測量時間`, `腳圍`) VALUES
('A001', '001', '2024-09-11 15:05:31', 50),
('A002', '001', '2024-09-11 15:05:32', 90),
('A003', '003', '2024-09-11 12:30:00', 30);

CREATE TABLE `病患資料` (
  `等級` TEXT DEFAULT NULL,
  `病患_ID` TEXT NOT NULL,
  `名字` TEXT DEFAULT NULL,
  `性別` TEXT DEFAULT NULL,
  `身高` FLOAT DEFAULT NULL,
  `病患_LineID` TEXT DEFAULT NULL,
  PRIMARY KEY (`病患_ID`)
);

INSERT INTO `病患資料` (`等級`, `病患_ID`, `名字`, `性別`, `身高`, `病患_LineID`) VALUES
('A', '001', '高翊恩', '男', 172, 'n112233'),
('B', '002', '李子捷', '男', 168, 'j112233'),
('C', '003', '朱少謙', '男', 150, 'c112233');

CREATE TABLE `病患體重` (
  `病患_ID` TEXT DEFAULT NULL,
  `體重` FLOAT DEFAULT NULL,
  FOREIGN KEY (`病患_ID`) REFERENCES `病患資料` (`病患_ID`)
);

INSERT INTO `病患體重` (`病患_ID`, `體重`) VALUES
('001', 59),
('002', 50),
('003', 120);

CREATE TABLE `腳圍資料` (
  `測量編號` TEXT DEFAULT NULL,
  `腳點1` DOUBLE DEFAULT NULL,
  `腳點2` DOUBLE DEFAULT NULL,
  `腳點3` DOUBLE DEFAULT NULL,
  `腳點4` DOUBLE DEFAULT NULL,
  `腳點5` DOUBLE DEFAULT NULL,
  `腳點6` DOUBLE DEFAULT NULL,
  `腳點7` DOUBLE DEFAULT NULL,
  `腳點8` DOUBLE DEFAULT NULL,
  `腳點9` DOUBLE DEFAULT NULL,
  `腳點10` DOUBLE DEFAULT NULL,
  `腳點11` DOUBLE DEFAULT NULL,
  `腳點12` DOUBLE DEFAULT NULL,
  `腳點13` DOUBLE DEFAULT NULL,
  `腳點14` DOUBLE DEFAULT NULL,
  `腳點15` DOUBLE DEFAULT NULL,
  `腳點16` DOUBLE DEFAULT NULL,
  `腳點17` DOUBLE DEFAULT NULL,
  `腳點18` DOUBLE DEFAULT NULL,
  `腳點19` DOUBLE DEFAULT NULL,
  `腳點20` DOUBLE DEFAULT NULL,
  `腳點21` DOUBLE DEFAULT NULL,
  `腳點22` DOUBLE DEFAULT NULL,
  `腳點23` DOUBLE DEFAULT NULL,
  `腳點24` DOUBLE DEFAULT NULL,
  `腳點25` DOUBLE DEFAULT NULL,
  `腳點26` DOUBLE DEFAULT NULL,
  `腳點27` DOUBLE DEFAULT NULL,
  `腳點28` DOUBLE DEFAULT NULL,
  `腳點29` DOUBLE DEFAULT NULL,
  `腳點30` DOUBLE DEFAULT NULL,
  `腳點31` DOUBLE DEFAULT NULL,
  `腳點32` DOUBLE DEFAULT NULL,
  FOREIGN KEY (`測量編號`) REFERENCES `水腫程度` (`測量編號`)
);

INSERT INTO `腳圍資料` (`測量編號`, `腳點1`, `腳點2`, `腳點3`, `腳點4`, `腳點5`, `腳點6`, `腳點7`, `腳點8`, `腳點9`, `腳點10`, `腳點11`, `腳點12`, `腳點13`, `腳點14`, `腳點15`, `腳點16`, `腳點17`, `腳點18`, `腳點19`, `腳點20`, `腳點21`, `腳點22`, `腳點23`, `腳點24`, `腳點25`, `腳點26`, `腳點27`, `腳點28`, `腳點29`, `腳點30`, `腳點31`, `腳點32`) VALUES
('A001', 0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, -27, 28, 29, 30, 31, 32, 33),
('A002', 0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, -27, 28, 29, 30, 31, 32, 33),
('A003', 0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, -27, 28, 29, 30, 31, 32, 33);

CREATE TABLE `醫生_病患關聯` (
  `醫生_ID` TEXT DEFAULT NULL,
  `病患_ID` TEXT DEFAULT NULL,
  FOREIGN KEY (`病患_ID`) REFERENCES `病患資料` (`病患_ID`),
  FOREIGN KEY (`醫生_ID`) REFERENCES `醫生資料` (`醫生_ID`)
);

INSERT INTO `醫生_病患關聯` (`醫生_ID`, `病患_ID`) VALUES
('D001', '001'),
('D001', '002'),
('D002', '002'),
('D002', '003');

CREATE TABLE `醫生資料` (
  `醫生_ID` TEXT NOT NULL,
  `名字` TEXT DEFAULT NULL,
  `醫生_LineID` TEXT DEFAULT NULL,
  `密碼` TEXT NOT NULL,
  PRIMARY KEY (`醫生_ID`)
);

INSERT INTO `醫生資料` (`醫生_ID`, `名字`, `醫生_LineID`, `密碼`) VALUES
('D001', '利侑謙', 'L112233', '123'),
('D002', '鄭羽雁', 'y112233', '123');
