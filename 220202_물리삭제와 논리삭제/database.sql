-- 필요한 데이터베이스와 테이블을 생성한다.
-- is_del열은 삭제플레그 열이다.
-- is_del열의 기본값은 0(False) 이다.


CREATE DATABASE snack CHARACTER SET UTF8;

use snack;

CREATE TABLE snack_delete(
    id     INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    name   VARCHAR(10) NOT NULL,
    is_del INT NOT NULL DEFAULT 0
)CHARSET=utf8;