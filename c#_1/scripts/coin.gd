extends Area2D
@onready var sfx_coin = $sfx_coin

func _on_body_entered(body: Node2D) -> void:
	sfx_coin.play()
	print("+1 coin!")
	queue_free()
