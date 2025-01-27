<script lang="ts">
	import '../app.css';
	let { children } = $props();
</script>

<div class="bg-custom-brown">
	<nav>
		<div class="flex justify-center items-center text-xl font-bold text-iris">
			<a class="mr-5 " href="/">Home</a>
			<a class="ml-5" href="/measure">Measurment Classification</a>
	</div>
	</nav>
	
</div>


{@render children()}
