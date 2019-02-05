<?php 
    /* 
        0: Brownsville
        1: Fort Stockton
        2: Victoria
        3: Amarillo
        4: El Dorado
        5: Dallas
        6: Houston
        7: Boston
        8: San Saba
        
        9: lasso
        10: Pijl en boog
        11: Gif
        12: Dynamiet
        13: Dolk
        14: Shotgun
        15: Revolver

        16: Hiawatha
        17: Pearl Hart
        18: Laura Ingalls
        19: Buffalo Bill
        20: Billy the Kid
        21: Clint Eastwood
    */

    function connectDatabase() {
        static $mysqli;
        $mysqli = new mysqli('localhost', 'u41868p37216_breakingbanks', 't3aTuQdUytJ9', 'u41868p37216_breakingbanks');
    	
    	if ($mysqli->connect_error) {
            exit("Connection failed: " . $mysqli->connect_error);
        } else {
            
        }
        
        return $mysqli;
    }

    function getIndexkaarten($game_code, $gebruiker_code) {
        $mysqli = connectDatabase();
        $result = "";
        
        $query = "SELECT kaarten FROM breakingbanks_kaarten WHERE game_code = ? AND gebruiker_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("ii", $game_code, $gebruiker_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();

            if($uitkomst->num_rows > 0) {
                while($myrow = $uitkomst->fetch_assoc()) {
                    $result = $myrow['kaarten'];
                }
            }
            $stmt->close();
        }
        return $result;
    }

    function extract_numbers($string) {
        preg_match_all('/([\d]+)/', $string, $match);
        return $match[0];
    }

    function verdeelKaarten($game_code) {
        $mysqli = connectDatabase();
        $winnendekaarten = "";
        $gebruikers = array();

        $query = "SELECT winnendekaarten as win FROM breakingbanks_game WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();

            if($uitkomst->num_rows > 0) {
                while($myrow = $uitkomst->fetch_assoc()) {
                    $winnendekaarten = $myrow['win'];
                }
            }
            $stmt->close();
        }        
        
        $kaarten = array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21");
        $winnendekaartenarray = extract_numbers($winnendekaarten);

        foreach($winnendekaartenarray as $winnendekaart) {
            $key = array_search($winnendekaart, $kaarten);
            unset($kaarten[$key]);
        }         

        $query = "SELECT gebruiker_code FROM breakingbanks_kaarten WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();
            
            if($uitkomst->num_rows > 0){
                while($myrow = $uitkomst->fetch_assoc()) {
                    array_push($gebruikers, $myrow['gebruiker_code']);
                }
            }
            $stmt->close();
        }

        $aantalgebruikers = count($gebruikers);
        

        while ($aantalgebruikers > 0) { 
            $aantalkaarten = round(count($kaarten) / $aantalgebruikers);
            $randomkaarten = array_rand($kaarten, $aantalkaarten);
            $mijnkaarten = "";

            foreach($randomkaarten as $randomkaart) {
                $mijnkaarten .= $randomkaart . " ";

                $key = array_search($randomkaart, $kaarten);
                unset($kaarten[$key]);
            }
            
            $query = "UPDATE breakingbanks_kaarten SET kaarten = ? WHERE game_code = ? AND gebruiker_code = ?";
            if($stmt = $mysqli->prepare($query)) {
                $stmt->bind_param("sii", $mijnkaarten, $game_code, $gebruikers[($aantalgebruikers-1)]);
                $stmt->execute();
                $stmt->close();
            }

            $aantalgebruikers -= 1;
        }
    }

    function createGamecode($gebruiker_code) {
        $mysqli = connectDatabase();
        $result = "";
        $winnendekaarten = "";

        $kaarten = array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21");
        
        $randomkaarten = array();
        $randomkaarten[0] = rand(0, 8);
        $randomkaarten[1] = rand(9, 15);
        $randomkaarten[2] = rand(16, 21);       
        
        foreach($randomkaarten as $randomkaart) {
            $winnendekaarten .= $randomkaart . " ";
            $key = array_search($randomkaart, $kaarten);
            unset($kaarten[$key]);
        }

        $query = "INSERT INTO breakingbanks_game (game_code, winnendekaarten, game_status) VALUES (NULL, ?, 'False')";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("s", $winnendekaarten);
            $stmt->execute();
            $stmt->close();
        }

        $query = "INSERT INTO breakingbanks_kaarten (gebruiker_code, game_code) SELECT ?, MAX(game_code) FROM breakingbanks_game";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $gebruiker_code);
            $stmt->execute();
            $stmt->close();
        }

        $query = "SELECT MAX(game_code) as maximaal FROM breakingbanks_game";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->execute();
            $uitkomst = $stmt->get_result();

            if($uitkomst > 0) {
                while($myrow = $uitkomst->fetch_assoc()) {
                    $result = $myrow['maximaal'];
                }
            }
            $stmt->close();
        }
        
        verdeelKaarten($result);
        return $result;
    }

    function joinGame($gebruiker_code, $game_code) {
        $mysqli = connectDatabase();
        $result = "";

        $query = "SELECT count(breakingbanks_kaarten.game_code) as aantal FROM breakingbanks_kaarten INNER JOIN breakingbanks_game ON breakingbanks_kaarten.game_code = breakingbanks_game.game_code WHERE breakingbanks_kaarten.game_code = ? and breakingbanks_game.game_status = 'False'";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();

            if($uitkomst->num_rows > 0) {
                while ($myrow = $uitkomst->fetch_assoc()) {
                    if($myrow['aantal'] == "0"){
                        return "0";
                    } elseif ($myrow['aantal'] == "6") {
                        return "0";
                    }
                }                
            } else {
                return "0";
            }
            $stmt->close();
        }
        
        $query = "INSERT INTO breakingbanks_kaarten (gebruiker_code, game_code) VALUES (?,?)";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("ii", $gebruiker_code, $game_code);
            $stmt->execute();
            $stmt->close();
        }

        verdeelKaarten($game_code);
        return $game_code;
    }

    function startGame($game_code) {
        $mysqli = connectDatabase();

        $query = "UPDATE breakingbanks_game SET game_status = 'True' WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $stmt->close();
            return "True";
        }
        return "False";
    }

    function statusGame($game_code) {
        $mysqli = connectDatabase();

        $query = "SELECT game_status FROM breakingbanks_game WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();

            if($uitkomst->num_rows > 0){
                while($myrow = $uitkomst->fetch_assoc()) {
                    return $myrow['game_status'];
                }
            } else {
                return "Over";
            }

            $stmt->close();
        }
    }

    function deleteGame($game_code) {
        $mysqli = connectDatabase();

        $query = "DELETE FROM breakingbanks_game WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $stmt->close();
        }

        $query = "DELETE FROM breakingbanks_kaarten WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $stmt->close();
        }
    }

    function verdeelKaarteneerlijk($game_code) {
        $mysqli = connectDatabase();
        $winnendekaarten = "";
        $uitgedeeldekaarten = "";
        $gebruikers = array();

        $query = "SELECT winnendekaarten as win FROM breakingbanks_game WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();

            if($uitkomst->num_rows > 0) {
                while($myrow = $uitkomst->fetch_assoc()) {
                    $winnendekaarten = $myrow['win'];
                }
            }
            $stmt->close();
        }        
        
        $kaarten = array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21");
        $winnendekaartenarray = extract_numbers($winnendekaarten);

        foreach($winnendekaartenarray as $winnendekaart) {
            $key = array_search($winnendekaart, $kaarten);
            unset($kaarten[$key]);
        }

        $query = "SELECT kaarten FROM breakingbanks_kaarten WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();

            if($uitkomst->num_rows > 0) {
                while($myrow = $uitkomst->fetch_assoc()) {
                    $uitgedeeldekaarten .= $myrow['kaarten'];
                }
            }
            $stmt->close();
        }   

        $uitgedeeldekaartenarray = extract_numbers($uitgedeeldekaarten);

        foreach($uitgedeeldekaartenarray as $uitgedeeldekaart) {
            $key = array_search($uitgedeeldekaart, $kaarten);
            unset($kaarten[$key]);
        }

        $query = "SELECT gebruiker_code FROM breakingbanks_kaarten WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();
            
            if($uitkomst->num_rows > 0){
                while($myrow = $uitkomst->fetch_assoc()) {
                    array_push($gebruikers, $myrow['gebruiker_code']);
                }
            }
            $stmt->close();
        }

        $aantalgebruikers = count($gebruikers);

        while ($aantalgebruikers > 0) {
            $aantalkaarten = round(count($kaarten) / $aantalgebruikers);
            $randomkaarten = array_rand($kaarten, $aantalkaarten);
            $mijnkaarten = "";

            foreach($randomkaarten as $randomkaart) {
                $mijnkaarten .= $randomkaart . " ";

                $key = array_search($randomkaart, $kaarten);
                unset($kaarten[$key]);
            }            

            $query = "UPDATE breakingbanks_kaarten SET kaarten = CONCAT(kaarten, '$mijnkaarten') WHERE game_code = ? AND gebruiker_code = ?";
            if($stmt = $mysqli->prepare($query)) {
                $stmt->bind_param("ii", $game_code, $gebruikers[($aantalgebruikers-1)]);
                $stmt->execute();
                $stmt->close();
            }

            $dekaarten = "";
            $query = "SELECT kaarten FROM breakingbanks_kaarten WHERE game_code = ? AND gebruiker_code = ?";
            if($stmt = $mysqli->prepare($query)) {
                $stmt->bind_param("ii", $game_code, $gebruikers[($aantalgebruikers-1)]);
                $stmt->execute();
                $uitkomst = $stmt->get_result();

                if($uitkomst->num_rows > 0) {
                    while($myrow = $uitkomst->fetch_assoc()) {
                        $dekaarten = $myrow['kaarten']; 
                    }
                }
                $stmt->close();
            }
            
            $dekaartenarray = extract_numbers($dekaarten);
            sort($dekaartenarray);

            $dekaarten = "";
            foreach($dekaartenarray as $dekaart) {
                $dekaarten .= $dekaart . " ";
            }

            $query = "UPDATE breakingbanks_kaarten SET kaarten = ? WHERE game_code = ? AND gebruiker_code = ?";
            if($stmt = $mysqli->prepare($query)) {
                $stmt->bind_param("sii", $dekaarten, $game_code, $gebruikers[($aantalgebruikers-1)]);
                $stmt->execute();
                $stmt->close();
            }

            $aantalgebruikers -= 1;
        }
    }

    function leaveGame($game_code, $gebruiker_code) {
        $mysqli = connectDatabase();
        $query = "DELETE FROM breakingbanks_kaarten WHERE game_code = ? AND gebruiker_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("ii", $game_code, $gebruiker_code);
            $stmt->execute();
            $stmt->close();
        }

        $query = "SELECT COUNT(*) as aantal FROM breakingbanks_kaarten WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();

            if($uitkomst->num_rows > 0) {
                while($myrow = $uitkomst->fetch_assoc()) {
                    if($myrow['aantal'] == "0") {
                        deleteGame($game_code);
                    } else {
                        verdeelKaarteneerlijk($game_code);
                    }
                }
            }
            $stmt->close();
        }
    }

    function getDice($game_code) {
        $mysqli = connectDatabase();
        $result = "";
        $query = "SELECT dobbelsteen, dobbelsteen2 FROM breakingbanks_game WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();

            if($uitkomst->num_rows > 0) {
                while($myrow = $uitkomst->fetch_assoc()) {
                    $result = $myrow['dobbelsteen'] . " " . $myrow['dobbelsteen2'];
                }
            }
        }
        return $result;
    }

    function updateDice($dice1, $dice2, $game_code) {
        $mysqli = connectDatabase();

        $query = "UPDATE breakingbanks_game SET dobbelsteen = ?, dobbelsteen2 = ? WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("iii", $dice1, $dice2, $game_code);
            $stmt->execute();
            $stmt->close();
        }
    }

    function stuurkaarten($game_code, $gebruiker_code, $kaart1, $kaart2, $kaart3) {
        $mysqli = connectDatabase();
        $winnendekaarten = "";
        $mijnkaarten = "";

        $query = "SELECT winnendekaarten as win FROM breakingbanks_game WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();

            if($uitkomst->num_rows > 0) {
                while($myrow = $uitkomst->fetch_assoc()) {
                    $winnendekaarten = $myrow['win'];
                }
            }
            $stmt->close();
        }        
        
        $kaarten = array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21");
        $winnendekaartenarray = extract_numbers($winnendekaarten);

        foreach($winnendekaartenarray as $winnendekaart) {
            $key = array_search($winnendekaart, $kaarten);
            unset($kaarten[$key]);
        }  
        

        $query = "SELECT kaarten FROM breakingbanks_kaarten WHERE game_code = ? AND gebruiker_code = ?";
        if($stmt = $mysqli->prepare($query)) {
            $stmt->bind_param("ii", $game_code, $gebruiker_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();

            if($uitkomst->num_rows > 0) {
                while($myrow = $uitkomst->fetch_assoc()) {
                    $mijnkaarten = $myrow['kaarten'];
                }
            }
            $stmt->close();
        } 

        $mijnkaartenarray = extract_numbers($mijnkaarten);
        foreach($mijnkaartenarray as $mijnkaart) {
            $key = array_search($mijnkaart, $kaarten);
            unset($kaarten[$key]);
        }
        
        shuffle($kaarten);

        foreach($kaarten as $kaart) {
            if ($kaart1 == $kaart) {
                return $kaart;
            } elseif ($kaart2 == $kaart) {
                return $kaart;
            } elseif ($kaart3 == $kaart) {
                return $kaart;
            }
        }

        return "22";
    }

    function finalanswer($game_code, $gebruiker_code, $kaart1, $kaart2, $kaart3) {
        $mysqli = connectDatabase();
        $winnendekaarten = "";

        $query = "SELECT winnendekaarten FROM breakingbanks_game WHERE game_code = ?";
        if($stmt = $mysqli->prepare($query)){
            $stmt->bind_param("i", $game_code);
            $stmt->execute();
            $uitkomst = $stmt->get_result();

            if($uitkomst->num_rows > 0) {
                while($myrow = $uitkomst->fetch_assoc()) {
                    $winnendekaarten = $myrow['winnendekaarten'];
                }
            }
        }
        $winnendekaartenarray = extract_numbers($winnendekaarten);
        if($kaart1 == $winnendekaartenarray[0] && $kaart2 == $winnendekaartenarray[1] && $kaart3 == $winnendekaartenarray[2]) {
            deleteGame($game_code);
            return "True";
        } else {
            leaveGame($game_code, $gebruiker_code);
        }
        // return boolean True als het klopt anders False
    }

    if(isset($_GET['actie'])){
        if($_GET['actie'] == "getindexkaarten"){
            if(isset($_GET['code'])) {
                if(isset($_GET['gebruiker'])) {
                    echo getIndexkaarten($_GET['code'], $_GET['gebruiker']);
                }
            }
        } elseif($_GET['actie'] == "creategamecode") {
            if(isset($_GET['gebruiker'])) {
                echo createGamecode($_GET['gebruiker']);
            }
        } elseif($_GET['actie'] == "joingame") {
            if(isset($_GET['gebruiker'])) {
                if(isset($_GET['code'])) {
                    echo joinGame($_GET['gebruiker'], $_GET['code']);
                }
            }
        } elseif($_GET['actie'] == "startgame") {
            if(isset($_GET['code'])) {
                echo startGame($_GET['code']);
            }
        } elseif($_GET['actie'] == "statusgame") {
            if(isset($_GET['code'])) {
                echo statusGame($_GET['code']);
            }
        } elseif($_GET['actie'] == "leavegame") {
            if(isset($_GET['code'])) {
                if(isset($_GET['gebruiker'])) {
                    echo leaveGame($_GET['code'], $_GET['gebruiker']);
                }
            }
        } elseif($_GET['actie'] == "getdice") {
            if(isset($_GET['code'])) {
                echo getDice($_GET['code']);
            }
        } elseif($_GET['actie'] == "updatedice") {
            if(isset($_GET['een'])) {
                if(isset($_GET['twee'])) {
                    if(isset($_GET['code'])) {
                        updateDice($_GET['een'], $_GET['twee'], $_GET['code']);
                    }
                }
            }
        } elseif($_GET['actie'] == "final") {
            if(isset($_GET['code'])) {
                if (isset($_GET['gebruiker'])) {
                    if (isset($_GET['kaart1'])) {
                        if (isset($_GET['kaart2'])) {
                            if (isset($_GET['kaart3'])) {
                                echo finalanswer($_GET['code'], $_GET['gebruiker'], $_GET['kaart1'], $_GET['kaart2'], $_GET['kaart3']);
                            }
                        }
                    }
                }
            }
        } elseif($_GET['actie'] == "stuurkaarten") {
            if(isset($_GET['code'])) {
                if (isset($_GET['gebruiker'])) {
                    if (isset($_GET['kaart1'])) {
                        if (isset($_GET['kaart2'])) {
                            if (isset($_GET['kaart3'])) {
                                echo stuurkaarten($_GET['code'], $_GET['gebruiker'], $_GET['kaart1'], $_GET['kaart2'], $_GET['kaart3']);
                            }
                        }
                    }
                }
            }
        }
    }
?>