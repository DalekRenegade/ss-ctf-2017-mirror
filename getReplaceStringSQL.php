<?php
function prepare1995Sql_EXAMPLE ($sqlString) {

    # regex pattern
    $patterns = array();
    $patterns[0] = '/\'.*?\'/';
    $patterns[1] = '/\$([a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)/';

    # best to use question marks for an easy example
    $replacements = array();
    $replacements[0] = '?';

    # perform replace
    $temp_preparedSqlString = preg_replace($patterns[0], $replacements[0], $sqlString);
    $preparedSqlString = preg_replace($patterns[1], $replacements[0], $temp_preparedSqlString);

    # grab parameter values
    $pregMatchAllReturnValueHolder = preg_match_all($patterns[0], $sqlString, $grabbedParameterValues);
    $pregMatchAllReturnValueHolder1 = preg_match_all($patterns[1], $sqlString, $grabbedParameterValues1);
    $parameterValues = $grabbedParameterValues[0];
    $parameterValues1 = $grabbedParameterValues1[0];

    # prepare command:
    echo('$stmt = $pdo->prepare("' . $preparedSqlString . '");');
    echo("\n");

    # binding of parameters
    $bindValueCtr = 1;
    foreach($parameterValues as $key => $value) {
    echo('$stmt->bindParam(' . $bindValueCtr . ", " . $value . ");");
    echo("\n");
    $bindValueCtr++;
    }
    foreach($parameterValues1 as $key => $value) {
    echo('$stmt->bindParam(' . $bindValueCtr . ", " . $value . ");");
    echo("\n");
    $bindValueCtr++;
    }

    # if you want to add the execute part, simply:
    echo('$stmt->execute();');
}

$sqlString = $argv[1];
prepare1995Sql_EXAMPLE ($sqlString);
?>
