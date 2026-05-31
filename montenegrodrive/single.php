<?php
/**
 * Single post template
 *
 * @package MontenegroDrive
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

get_header();
?>

<?php while ( have_posts() ) : the_post(); ?>

    <article id="post-<?php the_ID(); ?>" <?php post_class( 'max-w-container-max mx-auto px-gutter py-section-padding' ); ?>>

        <header class="mb-stack-lg">
            <h1 class="font-h1 text-h1 text-primary mb-stack-md"><?php the_title(); ?></h1>
            <div class="text-body-sm text-secondary flex gap-4 items-center">
                <span><?php echo esc_html( get_the_date() ); ?></span>
                <span aria-hidden="true">·</span>
                <span><?php echo esc_html( get_the_author() ); ?></span>
            </div>
        </header>

        <?php if ( has_post_thumbnail() ) : ?>
            <div class="mb-stack-lg rounded-xl overflow-hidden shadow-sm">
                <?php the_post_thumbnail( 'full', array( 'class' => 'w-full h-auto' ) ); ?>
            </div>
        <?php endif; ?>

        <div class="prose max-w-none">
            <?php the_content(); ?>
        </div>

    </article>

    <?php if ( comments_open() || get_comments_number() ) : ?>
        <div class="max-w-container-max mx-auto px-gutter py-stack-lg">
            <?php comments_template(); ?>
        </div>
    <?php endif; ?>

<?php endwhile; ?>

<?php get_footer();
