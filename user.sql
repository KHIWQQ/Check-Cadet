SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `user` (
  `user` varchar(33) NOT NULL,
  `pass` varchar(33) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `user` (`user`, `pass`) VALUES
('a', 'a'),
('b', 'b'),
('c', 'c'),
('admin', 'admin');
COMMIT;

