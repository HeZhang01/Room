<?php

class A {
	public function __construct() {
		echo 'A';
	}
}

class B extends A {
	public function __construct() {
		echo 'B';
	}
}

new B();
