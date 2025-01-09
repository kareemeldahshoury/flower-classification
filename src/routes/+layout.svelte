<script lang="ts">
	import '../app.css';
	let { children } = $props();
</script>

<div class="">
	<nav>
		<a href="/">Home</a>
		<a href="/measure">Measurment Classification</a>
	</nav>
	
</div>


{@render children()}
