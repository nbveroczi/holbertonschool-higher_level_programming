//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var textfield_number: UITextField!

    @IBAction func clickPlayButton (sender: UIButton!){

        image_tapper.hidden = true
        button_play.hidden = true
        textfield_number.hidden = true


        if textfield_number.text <= nil ||
        textfield_number.text != "" {
            print("Let's do" ,textfield_number.text, "taps")

        }
    }


}
